import xbmc
import xbmcgui
import os

import tardis
import sfile

import zipfile

HOME  = xbmc.translatePath('special://profile/')
LINE1 = 'Backup file now being created.'
LINE2 = 'Please wait, this may take a while.'


def doBackup(backup):
    CUSTOM = '1'

    chanType = tardis.GetSetting('chan.type')
    logoType = tardis.GetSetting('logo.type')
    
    tardis.log('Backup: Channel setting is %s' % chanType)
    tardis.log('Backup: Logo setting is %s' % logoType)

    if (chanType == CUSTOM) or (logoType == CUSTOM):
        tardis.DialogOK('It appears you are using a custom location', 'for your channels or logos (Home Networking).', 'Please back-up Tardis TV manually.')
        return

    try:
        folder = getFolder('Please select a back-up folder location')

        if not folder:
            return False

        backupName = ''

        if backup == 'full':
            backupName = getText('Please enter a name for your full back-up', backupName)
        else:
            backupName = getText('Please enter a name for your line-up', backupName)

        filename = os.path.join(folder, backupName + '.zip')

        dp = tardis.Progress(LINE1, LINE2)

        success = doZipfile(backup, filename, dp)

        dp.close()

        if success: 
            tardis.DialogOK('Back-up successfully created')
        else:
            tardis.DeleteFile(filename)

        return True

    except Exception, e:
        tardis.log(e)

    return False


def doZipfile(backup, outputFile, dp):
    zip = None

    if backup == 'full':
        ROOT = tardis.PROFILE
    else:
        ROOT = os.path.join(tardis.PROFILE, 'channels')

    source  = ROOT
    relroot = os.path.abspath(os.path.join(source, os.pardir))

    total = float(0)
    index = float(0)

    for root, dirs, files in os.walk(source):
        total += 1
        for file in files:
            total += 1

    for root, dirs, files in os.walk(source):
        if zip == None:
            zip = zipfile.ZipFile(outputFile, 'w', zipfile.ZIP_DEFLATED)

        index   += 1
        percent  = int(index / total * 100)
        if not updateProgress(dp, percent):
            return False

        local = os.path.relpath(root, relroot)

        for file in files:
            index   += 1
            percent  = int(index / total * 100)
            if not updateProgress(dp, percent):
                return False

            arcname  = os.path.join(local, file)
            filename = os.path.join(root, file)
            zip.write(filename, arcname)

    return True


def updateProgress(dp, percent):
    dp.update(percent, LINE1, LINE2)
    if not dp.iscanceled():
        return True

    return False


def getFolder(title):
    root   = xbmc.translatePath('special://userdata').split(os.sep, 1)[0] + os.sep
    folder = xbmcgui.Dialog().browse(3, title, 'files', '', False, False, root)

    return xbmc.translatePath(folder)


def getText(title, text='', hidden=False):
    kb = xbmc.Keyboard(text, title)
    kb.setHiddenInput(hidden)
    kb.doModal()
    if not kb.isConfirmed():
        return None

    text = kb.getText().strip()

    if len(text) < 1:
        return None

    return text


if __name__ == '__main__':
    try:
        backup = sys.argv[1]
        doBackup(backup)
    except: pass

