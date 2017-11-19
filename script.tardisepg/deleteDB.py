import os
import xbmc
import xbmcgui
import xbmcaddon
import settings
import tardis

settingsFile = xbmc.translatePath(os.path.join(tardis.PROFILE, 'settings.cfg'))


def deleteDB():
    try:
        import glob
        tardis.log('Deleting database...')
        dbPath  = tardis.PROFILE
        dbFile  = os.path.join(dbPath, 'program.db')
        delete_file(dbFile)

        passed  = not os.path.exists(dbFile)

        if passed: 
            tardis.log('Deleting database...PASSED')
            import update
            update.checkForUpdate(silent = True)
        else:
            tardis.log('Deleting database...FAILED')

        return passed

    except Exception, e:
        tardis.log('Deleting database...EXCEPTION %s' % str(e))
        return False

def delete_file(filename):
    tardis.SetSetting('epg.date', '2000-01-01')
    tries = 10
    while os.path.exists(filename) and tries > 0:
        settings.set('ChannelsUpdated', 0, settingsFile)
        try:
            os.remove(filename) 
            break 
        except: 
            tries -= 1 

if __name__ == '__main__':
    tardis.ShowBusy()
    
    if deleteDB():
        tardis.CloseBusy()
        tardis.DialogOK('EPG successfully reset.', 'It will be re-created next time', 'you start the guide')    
    
    else:
        tardis.CloseBusy()
        d = xbmcgui.Dialog()
        tardis.DialogOK('Failed to reset EPG.', 'Database may be locked,', 'please restart Kodi and try again')