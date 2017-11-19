import xbmc
import xbmcgui
import xbmcaddon

import gui

ADDON = xbmcaddon.Addon(id = 'script.tardisepg')


def changeListings():
    gui.close()
    ADDON.openSettings(ADDON)
    xbmc.executebuiltin('XBMC.ActivateWindow(home)')
    w = gui.TVGuide()

    w.doModal()
    del w
    
    
    changeListings()
