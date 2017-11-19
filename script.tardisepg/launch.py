import xbmc
import xbmcaddon
import xbmcgui
import urllib
import urllib2
from hashlib import md5
import socket
import os
import re
import shutil
import datetime
import download
import extract
import update
import tardis
import catchup
import sfile

import settings
settings.validate()


ADDON       = tardis.ADDON
HOME        = tardis.HOME
TITLE       = tardis.TITLE
VERSION     = tardis.VERSION

skin        = tardis.SKIN
addonpath   = tardis.RESOURCES
datapath    = tardis.PROFILE
extras      = os.path.join(datapath,   'extras')
skinfolder  = os.path.join(extras,     'skins')
dest        = os.path.join(skinfolder, 'skins.zip')
default_ini = os.path.join(addonpath,  'addons.ini')
local_ini   = os.path.join(addonpath,  'local.ini')
current_ini = os.path.join(datapath,   'addons.ini')
database    = os.path.join(datapath,   'program.db')
channel_xml = os.path.join(addonpath,  'chan.xml')
image       = xbmcgui.ControlImage

FIRSTRUN = tardis.GetSetting('FIRSTRUN') == 'true'


def CheckVersion():
    prev = tardis.GetSetting('VERSION')
    curr = VERSION
    tardis.log('****** TardisEPG %s LAUNCHED ******' % str(VERSION))

    if prev == curr:
        return

    tardis.SetSetting('VERSION', curr)

    if not tardis.isDSF():
        tardis.DialogOK('Welcome to Tardis TV', 'For online support, please join our Facebook Group:', 'https://www.facebook.com/groups/tardisbuilds/')
        showChangelog()


def showChangelog(addonID=None):
    try:
        f     = open(ADDON.getAddonInfo('changelog'))
        text  = f.read()
        title = '%s - %s' % (xbmc.getLocalizedString(24054), ADDON.getAddonInfo('name'))

        showText(title, text)

    except:
        pass


def showText(heading, text):
    id = 10147

    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(100)

    win = xbmcgui.Window(id)

    retry = 50
    while (retry > 0):
        try:
            xbmc.sleep(10)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            # return
        except:
            pass


def CheckForChannels():
    dir    = tardis.GetChannelFolder()
    folder = os.path.join(dir, 'channels')
    files  = []
    try:    current, dirs, files = sfile.walk(folder)
    except: pass
    if len(files) == 0:
        tardis.SetSetting('updated.channels', -1) # force refresh of channels


def CheckForUpdate():
    if xbmcgui.Window(10000).getProperty('TTV_UPDATING') != 'True':
        import update
        update.checkForUpdate(silent = True)
        return

    while xbmcgui.Window(10000).getProperty('TTV_UPDATING') == 'True':
        xbmc.sleep(1000)


def CheckDSF():
    try:
        if not tardis.isDSF():
            return

        dsf  = tardis.DSF
        path = dsf.getAddonInfo('path')

        sys.path.insert(0, path)
        import gvax

        xml      = gvax.getCatsXML()
        filename = os.path.join(datapath, 'cats.xml')

        f = file(filename, 'w')
        f.write(xml)
        f.close()

        xml      = gvax.getChannelsXML()
        filename = os.path.join(datapath, 'chan.xml')

        f = file(filename, 'w')
        f.write(xml)
        f.close()
        
    except:
        pass


def CopyKeymap():
    return
    src = os.path.join(xbmc.translatePath('special://userdata/keymaps'), 'zTTV.xml')
    if os.path.exists(src):
        os.remove(src)

    src = os.path.join(xbmc.translatePath('special://userdata/keymaps'), 'super_favourites_menu.xml')

    if not os.path.exists(src):
        return

    dst = os.path.join(xbmc.translatePath(ADDON.getAddonInfo('profile')), 'super_favourites_menu.xml')

    import shutil
    shutil.copyfile(src, dst)

    os.remove(src)

    xbmc.sleep(1000)
    xbmc.executebuiltin('Action(reloadkeymaps)')


def RemoveKeymap():
    return
    src = os.path.join(xbmc.translatePath(ADDON.getAddonInfo('profile')), 'super_favourites_menu.xml')

    if not os.path.exists(src):
        return

    dst = os.path.join(xbmc.translatePath('special://userdata/keymaps'), 'super_favourites_menu.xml')

    import shutil
    shutil.copyfile(src, dst)

    os.remove(src)

    xbmc.sleep(1000)
    xbmc.executebuiltin('Action(reloadkeymaps)')


def main(doLogin=True):
    import message
    if tardis.FirstRun():
        tardis.ShowBusy()
    import gui

    try:
        if not tardis.validToRun():
            tardis.CloseBusy()
            tardis.notify('Failed to obtain a response from Tardis TV')
            return

        CheckVersion()
#        if not FIRSTRUN:
        CheckForUpdate()
        CheckDSF()
        CheckForChannels()

        tardis.log('****** Tardis EPG - All OK *******')

        message.check()
        tardis.CloseBusy()

        xbmcgui.Window(10000).setProperty('TTV_RUNNING', 'True')
        xbmcgui.Window(10000).clearProperty('TTV_CATCHUP')

        w = gui.TVGuide()

        CopyKeymap()
        w.doModal()
        RemoveKeymap()
        del w

        xbmcgui.Window(10000).clearProperty('TTV_RUNNING')
        xbmcgui.Window(10000).clearProperty('TTV_WINDOW')

    except Exception:
        raise


kodi = True
if xbmcgui.Window(10000).getProperty('TTV_KODI').lower() == 'false':
    kodi = False
xbmcgui.Window(10000).clearProperty('TTV_KODI')


#Reset Now/Next information
xbmcgui.Window(10000).setProperty('TTV_NOW_TITLE',  '')
xbmcgui.Window(10000).setProperty('TTV_NOW_TIME',   '')
xbmcgui.Window(10000).setProperty('TTV_NEXT_TITLE',  '')
xbmcgui.Window(10000).setProperty('TTV_NEXT_TIME',   '')


#Initialise the window ID that was used to launch TTV (needed for SF functionality)
xbmcgui.Window(10000).setProperty('TTV_LAUNCH_ID', str(xbmcgui.getCurrentWindowId()))

main(kodi)
