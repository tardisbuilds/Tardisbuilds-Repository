import xbmc
import xbmcaddon
import download
import extract
import datetime
import os

import tardis

ADDON    = xbmcaddon.Addon(id = 'script.tardisepg')
datapath = xbmc.translatePath(ADDON.getAddonInfo('profile'))
extras   = os.path.join(datapath, 'extras')
logos    = os.path.join(extras, 'logos')
nologos  = os.path.join(logos, 'None')
dest     = os.path.join(extras, 'logos.zip')
logopack = tardis.GetSetting('tardis.logo.folder')
url      = tardis.GetExtraUrl() + 'resources/logos.zip'


try:
    if not os.path.exists(logos):
        os.makedirs(logos)
        os.makedirs(nologos)
except:
    pass
 
download.download(url, dest)

if os.path.exists(logos):
    now  = datetime.datetime.now()
    date = now.strftime('%B-%d-%Y %H-%M')
    
    import shutil
    cur = tardis.GetSetting('tardis.logo.folder')
    src = os.path.join(logos, cur)
    dst = os.path.join(logos, cur+'-%s' % date)
    
    try:
        shutil.copytree(src, dst)
        shutil.rmtree(src)
    except:
        pass
    
    extract.all(dest, extras)

try:
    os.remove(dest)
except:
    pass