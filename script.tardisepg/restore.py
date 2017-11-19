import xbmc
import xbmcgui
import xbmcaddon
import os

import tardis

import zipfile

HOME  = xbmc.translatePath('special://profile/')
LINE1 = 'Now restoring from backup'
LINE2 = 'Please wait, this may take a while.'


def doRestore(restore):
    try:
        filename = getFile('Please select back-up file', 'zip')

        if not filename:
            return False

        dp = tardis.Progress(LINE1, LINE2, hide=True)

        success = extractAll(restore, filename, dp)

        dp.close()

        if success: 
            tardis.DialogOK('Backup successfully restored')

        return True

    except Exception, e:
        tardis.log(e)

    return False


def extractAll(restore, filename, dp):
    tardis.log('------------------------------------------------')
    tardis.log(restore)
    zin = zipfile.ZipFile(filename, 'r')

    if restore == 'full':
        ROOT   = tardis.PROFILE
        folder = ROOT.rsplit('script.tardisepg', 1)[0]
        tardis.log(ROOT)
        tardis.log(folder)
        tardis.log(filename)
    else:
        ROOT   = os.path.join(tardis.PROFILE, 'channels')
        folder = ROOT.rsplit('channels', 1)[0]

    try:
        nItem = float(len(zin.infolist()))
        index = 0
        for item in zin.infolist():
            index += 1

            percent  = int(index / nItem *100)
            dp.update(percent, LINE1, LINE2)

            zin.extract(item, folder)
            # else:
            #     zin.extract(item, ROOT)

    except Exception, e:
        tardis.log('Error whilst unzipping %s' % zin.filename)
        tardis.log(e)
        return False

    return True


def getFile(title, ext):
    root     = xbmc.translatePath('special://userdata').split(os.sep, 1)[0] + os.sep
    filename = xbmcgui.Dialog().browse(1, title, 'files', '.'+ext, False, False, root)

    if filename == 'NO FILE':
        return None

    return filename


if __name__ == '__main__':
    try:
        restore = sys.argv[1]
        doRestore(restore)
    except: pass

    # xbmcaddon.Addon(tardis.ADDONID).openSettings()
