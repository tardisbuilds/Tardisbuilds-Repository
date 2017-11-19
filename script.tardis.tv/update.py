#
#      Copyright (C) 2015 Richard Dean
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#

import xbmcaddon
import xbmc
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

import json
import os

import sfile
import utilsTTV as utils


ADDON   = utils.ADDON
HOME    = utils.HOME
PROFILE = utils.PROFILE

AddonID = utils.AddonID
Addon   = utils.Addon
epghome = utils.epghome
epgpath = utils.epgpath
extras  = utils.extras
logos   = utils.logos

URL      = utils.getBaseURL() + 'ttv-update.txt'
FIRSTRUN = utils.getSetting('FIRSTRUN') == 'true'


def checkUpdate():
    if utils.isDSF():
        import dsf
        try:    dsf.checkUpdate()
        except: pass
        return
    
    if not FIRSTRUN:
        BASEURL = utils.getBaseURL()
        utils.doBackup()
        utils.downloadDefaults(BASEURL)
        try:
            cmd = 'XBMC.RunScript(special://home/addons/script.tardisepg/getIni.py)'
            xbmc.executebuiltin(cmd)
        except:
            pass
        return

    response = getResponse()
    if not response:
        utils.Log('Failed to get a response in checkUpdate')
        return

    try:    checkUpdateTTVSkin(response)
    except: pass

    try:    checkUpdateEPGSkin(response)
    except: pass

    try:    checkUpdateLogoColour(response)
    except: pass

    try:    checkUpdateLogoWhite(response)
    except: pass

    try:    checkUpdateTTV(response)
    except: pass

    try:    checkUpdateEPG(response)
    except: pass


def checkUpdateTTVSkin(response):
    if 'TTVSkin' not in response:
        return

    ttvskin = response['TTVSkin']

    curr = ttvskin
    prev = utils.getSetting('TTVSKIN')

    if prev == curr:
        return

    url     = utils.getBaseURL() + response['TTV Skin Link']
    path    = xbmc.translatePath(PROFILE) 
    path    = os.path.join(path, 'skins')
    zipfile = os.path.join(path, 'skin-update.zip')
        
    if not sfile.exists(path):
        sfile.makedirs(path)
        
    utils.downloadSkins(url, path, zipfile)
    utils.setSetting('TTVSKIN', curr)


def checkUpdateEPGSkin(response):
    if 'EPGSkin' not in response:
        return

    epgskin = response['EPGSkin']

    curr = epgskin
    prev = utils.getSetting('EPGSKIN')

    if prev == curr:
        return

    url     = utils.getBaseURL() + response['EPG Skin Link']
    path    = os.path.join(extras, 'skins')
    zipfile = os.path.join(path,   'skin-update.zip')
        
    if not sfile.exists(path):
        sfile.makedirs(path)
        
    utils.downloadSkins(url, path, zipfile)
    utils.setSetting('EPGSKIN', curr)


def checkUpdateLogoColour(response):
    if 'LogoColour' not in response:
        return

    logocolour = response['LogoColour']

    curr = logocolour
    prev = utils.getSetting('LOGOCOLOUR')

    if prev == curr:
        return

    url     = utils.getBaseURL() + response['Logo Colour']
    path    = os.path.join(logos, 'Colour Logo Pack')
    zipfile = os.path.join(path,  'logo-colour-update.zip')

    if not sfile.exists(path):
        sfile.makedirs(path)

    utils.downloadLogos(url, path, zipfile)
    utils.setSetting('LOGOCOLOUR', curr)


def checkUpdateLogoWhite(response):
    if 'LogoWhite' not in response:
        return

    logowhite = response['LogoWhite']

    curr = logowhite
    prev = utils.getSetting('LOGOWHITE')

    if prev == curr:
        return

    url     = utils.getBaseURL() + response['Logo White']
    path    = os.path.join(logos, 'White Logo Pack')
    zipfile = os.path.join(path,  'logo-white-update.zip')
        
    if not sfile.exists(path):
        sfile.makedirs(path)
        
    utils.downloadLogos(url, path, zipfile)
    utils.setSetting('LOGOWHITE', curr)


def checkUpdateTTV(response):
    if 'TTVUpdate' not in response:
        return

    ttvupdate = response['TTVUpdate']

    curr = ttvupdate
    prev = utils.getSetting('TTVUPDATE')

    if prev == curr:
        return

    url     = utils.getBaseURL() + response['TTV Update']
    path    = xbmc.translatePath(HOME)
    zipfile = os.path.join(path, 'python-update.zip')
        
    utils.doTTVUpdate(url, path, zipfile, ttvupdate)
    utils.setSetting('TTVUPDATE', curr)


def checkUpdateEPG(response):
    if 'EPGUpdate' not in response:
        return

    epgupdate = response['EPGUpdate']

    curr = epgupdate
    prev = utils.getSetting('EPGUPDATE')

    if prev == curr:
        return

    url     = utils.getBaseURL() + response['EPG Update']
    path    = xbmc.translatePath(epghome)
    zipfile = os.path.join(path, 'python-update.zip')
      
    if not sfile.exists(path):
        sfile.makedirs(path)
        
    utils.doEPGUpdate(url, path, zipfile, epgupdate)
    utils.setSetting('EPGUPDATE', curr)


def getResponse():
    try:
        request  = requests.get(URL, verify=False)
        response = request.content

        utils.Log('Response in checkUpdate %s' % str(response))

        return json.loads(u"" + (response))

    except:
        return None