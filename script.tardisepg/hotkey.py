import xbmc
import xbmcgui
import os

import tardis

def main():
    if not xbmcgui.Window(10000).getProperty('TTV_RUNNING') == 'TRUE':
        xbmcgui.Window(10000).setProperty('TTV_CATCHUP', 'TRUE')
        tardis.removeKeymap()

    name = os.path.join(tardis.HOME, 'osd.py')
    cmd  = 'RunScript(%s)' % (name)
    xbmc.executebuiltin(cmd)


if not xbmcgui.Window(10000).getProperty('TTV_OSD_RUNNING') == 'TRUE':
    main()