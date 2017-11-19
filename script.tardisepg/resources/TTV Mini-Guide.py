import xbmc

ADDONID = 'script.tardisepg'

def add(params):
    if xbmc.getCondVisibility('System.HasAddon(%s)' % ADDONID) == 1:
        return 'Tardis TV Mini-Guide'
    
    return None


def process(option, params):
    import xbmcaddon
    import os

    addon = xbmcaddon.Addon(ADDONID)
    path  = addon.getAddonInfo('path')

    script = os.path.join(path, 'osd.py')
    cmd    = 'RunScript(%s)' % script

    xbmc.executebuiltin(cmd)