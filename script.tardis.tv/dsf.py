# -*- coding: utf-8 -*-
#
#      Copyright (C) 2015 Richard Dean
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

DSFID   = utils.DSFID
DSF     = utils.DSF
DSFVER  = utils.DSFVER
home    = utils.home
profile = utils.profile

BASEURL  = utils.getBaseURL()
URL      = BASEURL + 'dsf-update.txt'
FIRSTRUN = utils.getSetting('FIRSTRUN') == 'true'

TOUCH   = 'script.video.gvax'
TCH_INSTALLED = xbmc.getCondVisibility('System.HasAddon(%s)' % TOUCH) == 1

def checkUpdate():
    if not TCH_INSTALLED:
        utils.DialogOK('Estimado cliente, por favor llame a su asesor GVAX para instalar la nueva presentacion')
        return
    if not FIRSTRUN:
        cmd = 'XBMC.RunScript(special://profile/autoexec-new.py)'
        xbmc.executebuiltin(cmd)
        return

        #utils.DialogOK('Bienvenido a GVAX', 'Ahora vamos a hacer una copia de seguridad de alguno de', 'los archivos existentes antes de la instalación.') 
        #doBackup()

        #Addon.setSetting('tardis.skin', 'EPG-Skin')
        #utils.setSetting('SKIN', 'TTV-Skin')

        #downloadDefaults(BASEURL)
        #return

    response   = getResponse()
    ttvskin    = response['DSFTTVSkin']
    epgskin    = response['DSFEPGSkin']
    logocolour = response['DSFLogos']
    ttvupdate  = response['DSFTTVUpdate']
    epgupdate  = response['DSFEPGUpdate']
    dsfupdate  = response['DSFUpdate']
    kodiskin   = response['DSFKodiSkin']

    curr = ttvskin
    prev = utils.getSetting('DSFTTVSKIN')

    if not prev == curr:
        url     = BASEURL + response['DSF TTV Skin']
        path    = xbmc.translatePath(PROFILE) 
        path    = os.path.join(path, 'skins')
        zipfile = os.path.join(path, 'dsf-skin-update.zip')
        
        if not sfile.exists(path):
            sfile.makedirs(path)
        
        downloadSkins(url, path, zipfile)
        utils.setSetting('DSFTTVSKIN', curr)


    curr = epgskin
    prev = utils.getSetting('DSFEPGSKIN')

    if not prev == curr:
        url     = BASEURL + response['DSF EPG Skin']
        path    = os.path.join(extras, 'skins')
        zipfile = os.path.join(path,   'dsf-skin-update.zip')
        
        if not sfile.exists(path):
            sfile.makedirs(path)
        
        downloadSkins(url, path, zipfile)
        utils.setSetting('DSFEPGSKIN', curr)


    curr = logocolour
    prev = utils.getSetting('DSFLOGOS')

    if not prev == curr:
        url     = BASEURL + response['DSF Logos']
        path    = os.path.join(logos, 'Colour Logo Pack')
        zipfile = os.path.join(path,  'dsf-logos-update.zip')
        
        if not sfile.exists(path):
            sfile.makedirs(path)
        
        downloadLogos(url, path, zipfile)
        utils.setSetting('DSFLOGOS', curr)


    curr = ttvupdate
    prev = utils.getSetting('DSFTTVUPDATE')

    if not prev == curr:
        url     = BASEURL + response['DSF TTV Update']
        path    = xbmc.translatePath(HOME)
        zipfile = os.path.join(path, 'dsf-ttv-python.zip')
        
        doTTVUpdate(url, path, zipfile, ttvupdate)
        utils.setSetting('DSFTTVUPDATE', curr)


    curr = epgupdate
    prev = utils.getSetting('DSFEPGUPDATE')

    if not prev == curr:
        url     = BASEURL + response['DSF EPG Update']
        path    = xbmc.translatePath(epghome)
        zipfile = os.path.join(path, 'dsf-epg-python.zip')
        
        if not sfile.exists(path):
            sfile.makedirs(path)
        
        doEPGUpdate(url, path, zipfile, epgupdate)
        utils.setSetting('DSFEPGUPDATE', curr)
    
    
    curr = dsfupdate
    prev = utils.getSetting('DSFUPDATE')

    if not prev == curr:
        url     = BASEURL + response['DSF Update']
        path    = xbmc.translatePath(home)
        zipfile = os.path.join(path, 'dsf-update.zip')
        
        if not sfile.exists(path):
            sfile.makedirs(path)
        
        doDSFUpdate(url, path, zipfile, dsfupdate)
        utils.setSetting('DSFUPDATE', curr)


def getResponse():
    request  = requests.get(URL, verify=False)
    response = request.content

    utils.Log('Response in checkUpdate %s' % str(response))

    return json.loads(u"" + (response))


def doBackup():
    import datetime
    
    src = os.path.join(epgpath, 'channels')
    dst = os.path.join(epgpath, 'channels-backup')
    
    try:
        sfile.remove(dst)
        sfile.copy(src, dst)
    except:
        pass
    
    if os.path.exists(logos):
        now  = datetime.datetime.now()
        date = now.strftime('%B-%d-%Y %H-%M')
    
        cur = Addon.getSetting('tardis.logo.folder')
        src = os.path.join(logos, cur)
        dst = os.path.join(logos, cur+'-%s' % date)
    
        try:
            sfile.rename(src, dst)
        except:
            pass


def downloadDefaults(url):
    import download
    import extract

    url1 = url + 'ttv/skins.zip'
    url2 = url + 'ttvepg/skins.zip'
    url3 = url + 'ttvepg/logos.zip'

    path1 = xbmc.translatePath(PROFILE)     # /addon_data/script.tardis.tv/
    path2 = os.path.join(epgpath, 'extras') # /addon_data/script.tardisepg/extras/
    path3 = os.path.join(path2,   'skins')
    path4 = os.path.join(path2,   'logos')

    zip1  = os.path.join(path1,   'skins.zip')
    zip2  = os.path.join(path2,   'skins.zip')
    zip3  = os.path.join(path2,   'logos.zip')

    if not sfile.exists(epgpath):
        sfile.makedirs(epgpath)

    if not sfile.exists(path1):
        sfile.makedirs(path1)
    download.download(url1, zip1)
    extract.all(zip1, path1, dp='Installing TTV skins')
    sfile.remove(zip1)

    if not sfile.exists(path2):
        sfile.makedirs(path2)
    download.download(url2, zip2)
    extract.all(zip2, path2, dp='Installing EPG skins')
    sfile.remove(zip2)

    if not sfile.exists(path4):
        sfile.makedirs(path2)
    download.download(url3, zip3)
    extract.all(zip3, path2)
    sfile.remove(zip3)

    Addon.setSetting('tardis.skin', 'EPG-Skin')
    utils.setSetting('SKIN', 'TTV-Skin')

    if utils.DialogYesNo('Would you like to assign a button ', 'on your remote control or keybord', 'to activate the Tardis TV Mini-Guide?'):
        xbmc.executebuiltin('RunScript(special://home/addons/script.tardisepg/keyProgrammer.py)')

    utils.setSetting('FIRSTRUN', 'true')


def downloadSkins(url, path, zipfile):
    import download
    import extract

    utils.DialogOK('Una nueva version actualizada está disponible.', 'Se puede descargar e instalar "," en su sistema GVAX.')

    download.download(url, zipfile)
    extract.all(zipfile, path, dp='Installing skin update')
    sfile.remove(zipfile)


def downloadLogos(url, path, zipfile):
    import download
    import extract

    utils.DialogOK('Algunos de los nuevos logotipos están disponibles.', 'Pueden ser descargados y añadidos a su logopack.')

    download.download(url, zipfile)
    extract.all(zipfile, path, dp='Installing logo update')
    sfile.remove(zipfile)


def doTTVUpdate(url, path, zipfile, ttvupdate):
    import download
    import extract

    utils.DialogOK('A GVAX "Live Update" está disponible.', 'Actualización será descargado e instalado en su sistema.', 'Gracias.')
    download.download(url, zipfile)
    extract.all(zipfile, path, dp='Installing python update')
    sfile.remove(zipfile)
    utils.Log('TTV Update %s installed' % str(ttvupdate))
    xbmc.executebuiltin('UpdateLocalAddons')


def doEPGUpdate(url, path, zipfile, epgupdate):
    import download
    import extract

    utils.DialogOK('Un GVAX EPG es "Live Update" disponible.', 'Actualización EPG será descargado e instalado en su sistema.', 'Gracias.')

    download.download(url, zipfile)
    extract.all(zipfile, path, dp='Installing python update')
    sfile.remove(zipfile)
    utils.Log('EPG Update %s installed' % str(epgupdate))
    xbmc.executebuiltin('UpdateLocalAddons')


def doDSFUpdate(url, path, zipfile, dsfupdate):
    import download
    import extract

    utils.DialogOK('Un GVAX es "Live Update" disponible.', 'Actualización será descargado e instalado en su sistema.', 'Gracias.')

    download.download(url, zipfile)
    extract.all(zipfile, path, dp='Installing python update')
    sfile.remove(zipfile)
    utils.Log('EPG Update %s installed' % str(dsfupdate))
    xbmc.executebuiltin('UpdateLocalAddons')