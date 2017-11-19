import os
import xbmc
import tardis
import resources

from resources.pastebin_python import PastebinPython
from resources.pastebin_python.pastebin_exceptions   import PastebinBadRequestException, PastebinNoPastesException, PastebinFileException
from resources.pastebin_python.pastebin_constants    import PASTE_PUBLIC, EXPIRE_10_MIN, EXPIRE_1_MONTH, EXPIRE_1_WEEK, PASTE_UNLISTED
from resources.pastebin_python.pastebin_formats      import FORMAT_NONE, FORMAT_PYTHON, FORMAT_HTML


def LogUploader():
    pastebin = PastebinPython(api_dev_key='69b5bba485b5ce76a20ec137e2565580')
    filename = os.path.abspath(getLogfile())

    tardis.log('------------ UPLOAD LOG ------------')
    tardis.log(filename)

    try:
        pastebin.createAPIUserKey('Tardis TV', 'tardisepg123')
        paste   = pastebin.createPasteFromFile(filename, 'Tardis TV Logfiles', FORMAT_HTML, PASTE_UNLISTED, EXPIRE_1_WEEK)
        logcode = paste.rsplit('/', 1)[-1]
        tardis.log(logcode)
 
        tardis.log(paste)
        tardis.DialogOK('This is your log code: [COLOR orange][B]' + logcode + '[/B][/COLOR]', 'Write it down and send it to us via our Facebook Page.', 'https://www.facebook.com/groups/tardisbuilds/')

    except PastebinBadRequestException as e:
        showError(e.message)
    except PastebinFileException as e:
        showError(e.message)


def showError(error):
    tardis.log(error)
    tardis.DialogOK('Sorry, the following error occurred:', '[COLOR orange][B]' + error + '[/B][/COLOR]', 'Restart Kodi and try again.')

def getLogfile():
    path = xbmc.translatePath('special://logpath')
    old  = os.path.join(path, 'xbmc.log')
    kodi = os.path.join(path, 'kodi.log')
    spmc = os.path.join(path, 'spmc.log')

    if os.path.isfile(old):
        tardis.log('======= Tardis TV log path is =======')
        tardis.log(old)
        return old

    if os.path.isfile(kodi):
        tardis.log('======= Tardis TV  log path is =======')
        tardis.log(kodi)
        return kodi

    if os.path.isfile(spmc):
        tardis.log('======= Tardis TV  log path is =======')
        tardis.log(spmc)
        return spmc


if __name__ == '__main__':
    tardis.ShowBusy()
    LogUploader()
    tardis.CloseBusy()
