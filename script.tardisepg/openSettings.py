import xbmcaddon
import xbmc
import xbmcgui
import os

import tardis

tardis.ADDON.openSettings()

xbmcgui.Window(10000).setProperty('TTV_KODI', 'false')

name   =  tardis.TITLE
script =  os.path.join(tardis.HOME, 'launch.py')
args   =  ''
cmd    = 'AlarmClock(%s,RunScript(%s,%s),%d,True)' % (name, script, args, 0)

xbmc.executebuiltin('CancelAlarm(%s,True)' % name)        
xbmc.executebuiltin(cmd)

