import xbmc
import xbmcaddon
import tardis

ttv = xbmcaddon.Addon('script.tardis.tv')

def getVersion():
    TTV  = ttv.getAddonInfo('version')
    TEPG = tardis.ADDON.getAddonInfo('version')

    tardis.DialogOK('You are currently running the following versions', 'Tardis TV: ' + '[COLOR orange][B]' + TTV + '[/B][/COLOR]', 'TardisEPG: ' + '[COLOR orange][B]' + TEPG + '[/B][/COLOR]')

    if tardis.DialogYesNo('Would you like to force Kodi to check', 'for any updates right now?', ''):
        xbmc.executebuiltin('UpdateAddonRepos')


if __name__ == '__main__':
    getVersion()
