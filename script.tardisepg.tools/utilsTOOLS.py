import xbmc
import xbmcaddon
import xbmcgui
import os
import re
import base64
import sfile


def GetXBMCVersion():
    #xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "method": "Application.GetProperties", "params": {"properties": ["version", "name"]}, "id": 1 }')

    version = xbmcaddon.Addon('xbmc.addon').getAddonInfo('version')
    version = version.split('.')
    return int(version[0]), int(version[1]) #major, minor


TITLE   = 'Tardis TV Tools'
ADDONID = 'script.tardisepg.tools'
ADDON   =  xbmcaddon.Addon(ADDONID)
HOME    =  ADDON.getAddonInfo('path')
PROFILE =  ADDON.getAddonInfo('profile')


TTV_TITLE   = 'Tardis TV'
TTV_ADDONID = 'script.tardisepg'
TTV_ADDON   =  xbmcaddon.Addon(TTV_ADDONID)
TTV_HOME    =  xbmc.translatePath(TTV_ADDON.getAddonInfo('path'))
TTV_PROFILE =  xbmc.translatePath(TTV_ADDON.getAddonInfo('profile'))


VERSION = ADDON.getAddonInfo('version')
ICON    = os.path.join(HOME, 'icon.png')
FANART  = os.path.join(HOME, 'fanart.jpg')
GETTEXT = ADDON.getLocalizedString


MAJOR, MINOR = GetXBMCVersion()
FRODO        = (MAJOR == 12) and (MINOR < 9)
GOTHAM       = (MAJOR == 13) or (MAJOR == 12 and MINOR == 9)

baseurl = base64.decodestring('aHR0cDovLzE2My4xNzIuNDYuMTIyL2ZpbGVzL2d1aWRlLw==')

def GetBaseUrl():
    return baseurl


def GetChannelType():
    return TTV_ADDON.getSetting('chan.type')


def GetChannelFolder():
    CUSTOM = '1'

    channelType = GetChannelType()

    if channelType == CUSTOM:
        path = TTV_ADDON.getSetting('user.chan.folder')
    else:
        path = TTV_PROFILE

    return path


channelFolder = GetChannelFolder()

TTV_CHANNELS  = os.path.join(channelFolder, 'channels')


def log(text):
    try:
        output = '%s V%s : %s' % (TITLE, VERSION, text)
        #print(output)
        xbmc.log(output, xbmc.LOGDEBUG)
    except:
        pass


def DialogOK(line1, line2='', line3=''):
    d = xbmcgui.Dialog()
    d.ok(TITLE + ' - ' + VERSION, line1, line2 , line3)


def DialogYesNo(line1, line2='', line3='', noLabel=None, yesLabel=None):
    d = xbmcgui.Dialog()
    if noLabel == None or yesLabel == None:
        return d.yesno(TITLE + ' - ' + VERSION, line1, line2 , line3) == True
    else:
        return d.yesno(TITLE + ' - ' + VERSION, line1, line2 , line3, noLabel, yesLabel) == True


def CheckVersion():
    prev = ADDON.getSetting('VERSION')
    curr = VERSION

    if prev == curr:        
        return

    ADDON.setSetting('VERSION', curr)

    if prev == '0.0.0' or prev == '1.0.0':
        folder  = xbmc.translatePath(PROFILE)
        try:
            if not sfile.isdir(folder):
                sfile.makedirs(folder) 
        except: pass

    #call showChangeLog like this to workaround bug in openElec
    script = os.path.join(HOME, 'showChangelog.py')
    cmd    = 'AlarmClock(%s,RunScript(%s),%d,True)' % ('changelog', script, 0)
    xbmc.executebuiltin(cmd)


def GetFolder(title):
    default = ''
    folder  = xbmc.translatePath(PROFILE)

    if not sfile.isdir(folder):
        sfile.makedirs(folder) 

    folder = xbmcgui.Dialog().browse(3, title, 'files', '', False, False, default)
    if folder == default:
        return None

    return xbmc.translatePath(folder)


def showBusy():
    busy = None
    try:
        import xbmcgui
        busy = xbmcgui.WindowXMLDialog('DialogBusy.xml', '')
        busy.show()

        try:    busy.getControl(10).setVisible(False)
        except: pass
    except:
        busy = None

    return busy


def clean(text):
    if not text:
        return None

    text = re.sub('[:\\\\/*?\<>|"]+', '', text)
    text = text.strip()
    if len(text) < 1:
        return  None

    return text


def deleteFile(path):
    tries = 5
    while os.path.exists(path) and tries > 0:
        tries -= 1 
        try: 
            sfile.remove(path) 
            break 
        except: 
            xbmc.sleep(500)


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
            return
        except:
            pass


def showChangelog(addonID=None):
    try:
        if addonID:
            ADDON = xbmcaddon.Addon(addonID)
        else: 
            ADDON = xbmcaddon.Addon(ADDONID)

        f     = open(ADDON.getAddonInfo('changelog'))
        text  = f.read()
        title = '%s - %s' % (xbmc.getLocalizedString(24054), ADDON.getAddonInfo('name'))

        showText(title, text)

    except:
        pass

if __name__ == '__main__':
    pass