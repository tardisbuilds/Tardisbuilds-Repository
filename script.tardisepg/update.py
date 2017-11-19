import xbmc
import xbmcgui
import os
import re
import datetime
import urllib2
import urllib
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

import json

import tardis
import sfile

#TARDISURL = tardis.GetSetting('tardis.url').upper()

username = tardis.GetUser()
password = tardis.GetPass()
response = ''

home       = tardis.HOME
datapath   = tardis.PROFILE
extras     = os.path.join(datapath, 'extras')
logos      = os.path.join(extras,   'logos')
logofolder = os.path.join(logos,    'None')
logodest   = os.path.join(logos,    'logos.zip')

cookiepath = os.path.join(datapath,   'cookies')
cookiefile = os.path.join(cookiepath, 'cookie')

try:
    #workaround Python bug in strptime which causes it to intermittently throws an AttributeError
    import datetime, time
    datetime.datetime.fromtimestamp(time.mktime(time.strptime('2013-01-01 19:30:00'.encode('utf-8', 'replace'), "%Y-%m-%d %H:%M:%S")))
except:
    pass



def generateMD5(path):
    if not sfile.exists(path):
        return '0'

    try:
        import hashlib        
        return hashlib.md5(sfile.read(path)).hexdigest()
    except:
        pass

    try:
        import md5
        return md5.new(sfile.read(path)).hexdigest()
    except:
        pass
        
    return '0'



def parseDate(dateString):
    if type(dateString) in [str, unicode]:            
        dt    = dateString.split('-')
        year  = int(dt[0])
        month = int(dt[1])
        day   = int(dt[2])
        return datetime.datetime(year, month, day, 0, 0, 0)

    return dateString



def deleteFile(filename, attempts = 5):
    while os.path.exists(filename) and (attempts > 0): 
        attempts -= 1
        try: 
            os.remove(filename) 
            break 
        except: 
            xbmc.sleep(100)


# -----------------------------------------------------------------------

def onBoot():
    tardis.log('onBoot')
    retry  = 12
    update = checkForUpdate(silent=True)

    while (not xbmc.abortRequested) and (not update) and (retry > 0):
        xbmc.sleep(5000)
        tardis.log('Failed to checkForUpdate (%d) - Trying again in 5 seconds' % retry)
        retry -= 1
        update = checkForUpdate(silent=True)

    tardis.log('onBoot returning %s' % str(update))
    return update


def checkForUpdate(silent = 1):
    # silent = 0
    xbmcgui.Window(10000).setProperty('TTV_UPDATING', 'True')

    silent = int(silent) == 1

    response = getResponse(silent)
    
    if 'Error' in response:
        if not silent:
            tardis.DialogOK('Oops! An error has occured: ', response['Error'], 'Please check your account at www.tardisbuilds.com')

        allDone(silent)
        return False
        
    isValid  = len(response) > 0

    if not isValid:
        if not silent:
            tardis.DialogOK('', 'No EPG update available.', 'Please try again later.')
        allDone(silent)
        return False
   
    try:
        if updateAvailable(response['Date']):
            tardis.log ('EPG Update Available - %s' % response['Date'])
            getUpdate(response, silent)

        else:
            # do restore to ensure not malformed
            # restoreFromZip()
            if not silent:
                tardis.DialogOK('EPG is up-to-date.')
    except:
        pass

    allDone(silent)

    return True


def allDone(silent, mins = 1 * 60 * 24): #24 hours
    try:    setAlarm(mins)
    except: pass

    xbmcgui.Window(10000).clearProperty('TTV_UPDATING')

    # if not silent:
    #     ADDON.openSettings()


def setAlarm(mins):
    #set script to run again in x minutes

    updateMins = mins
    addonPath  = home
    name       = tardis.TITLE + ' EPG Update'
    script     = os.path.join(addonPath, 'update.py')
    args       = '1' #silent
    cmd        = 'AlarmClock(%s,RunScript(%s,%s),%d,True)' % (name, script, args, updateMins)

    xbmc.executebuiltin('CancelAlarm(%s,True)' % name)
    xbmc.executebuiltin(cmd)
    tardis.log('TTV update timer started')


def getResponse(silent=False):
    URL = tardis.GetTardisUrl() + 'update.txt'
    tardis.log('============= TTV Update Check =============')

    request  = requests.get(URL, verify=False)
    code     = request.status_code
    response = request.content

    try:
        tardis.log ('TTV response status_code %s ' % code)
        return json.loads(u"" + (response))

    except Exception, e:
        tardis.log(e)
        return {'Error' : e}


def updateAvailable(latest):
    dir    = datapath
    folder = os.path.join(dir, 'channels')

    files = []
    try:    current, dirs, files = os.walk(folder).next()
    except: pass

    if len(files) == 0:
        tardis.SetSetting('updated.channels', -1) #force refresh of channels
        return True

    db  = os.path.join(dir, 'program.db')
    if not os.path.exists(db):
        return True

    current = tardis.GetSetting('epg.date')
    current = parseDate(current)
    latest  = parseDate(latest)
    update  = latest > current
    return update


def getUpdate(response, silent):
    try:
        link     = response['Link']
        md5      = response['MD5']
        date     = response['Date']
        channel  = response['Channel']
    except Exception, e:
        return

    path = getDownloadPath(date)

    db = path.replace('.newzip', '.db')
    if not os.path.exists(db):
        dp = None
    
        if not silent:
            dp = progress(TITLE, 'Updating EPG.', 'Please Wait.')

        try:
            download(link, path, dp)
        except:
            deleteFile(path) 
            return False  

        profile = datapath

        #delete existng zips files
        file = []
        try:    current, dirs, files = os.walk(profile).next()
        except: pass

        for file in files:
            if file.endswith('.zip'):
                filename = os.path.join(profile, file)
                deleteFile(filename)

        oldpath = path
        path    = path.replace('.newzip', '.zip')

        try:    os.rename(oldpath, path)
        except: pass

        #doesn't seem to want to work!
        #if generateMD5(path) != md5:
        #    deleteFile(path) 
        #    return False

        tardis.BackupCats()

        import dxmnew
        dxmnew.unzipAndMove(path, profile, None)

        #try:    deleteFile(path)
        #except: pass

    tardis.SetSetting('updated.channels', channel)

    #xbmcgui.Window(10000).setProperty('TTV_UPDATE', date)

    if xbmcgui.Window(10000).getProperty('TTV_RUNNING') == 'True':
        return

    newEPGAvailable(date)

    if not silent:
        ok(TITLE, '', 'EPG successfully updated.', '')


def restoreFromZip():
    profile = datapath

    file = []
    try:    current, dirs, files = os.walk(profile).next()
    except: pass

    for file in files:
        if file.endswith('.zip'):
            date = file.split('-', 1)[-1].replace('.zip', '')

            import dxmnew
            dxmnew.unzipAndMove(os.path.join(profile, file), profile, None)

            newEPGAvailable(date)
            return


def newEPGAvailable(date):
    dir = datapath
    deleteFile(os.path.join(dir, 'program.db'))

    dst = os.path.join(dir, 'program.db')
    src = os.path.join(dir, 'program-XXXXXX.db')
    src = src.replace('XXXXXX', date)

    try:
        os.rename(src, dst)
        deleteFile(src)
    except: pass

    tardis.SetSetting('epg.date', date)

    #xbmcgui.Window(10000).clearProperty('TTV_UPDATE')



def getDownloadPath(date):
    try:
        path = datapath
        path = xbmc.translatePath(path)
        path = os.path.join(path, 'program-%s.newzip' % date)
        return path
    except:
        pass

    return None



def download(url, dest, dp = None, start = 0, range = 100):
    tardis.log('============= listings status =============')
    #USER = tardis.GetUser()
    #PASS = tardis.GetPass()
    # request  = requests.post(URL, data=PAYLOAD)
    # response = request.content

    r = requests.get(url, auth=(tardis.GetUser(), tardis.GetPass()))
    code    = r.status_code
    content = r.content
    tardis.log(code)

    if not code == 200:
        content = content.replace('<strong>',  '')
        content = content.replace('</strong>', '')
        tardis.log('========== listings error  ==========')
        tardis.log(content)
        tardis.DialogOK('There was an error with the TV listings', 'Please contact support quoting the following error message:', '[COLOR orange][B]%s[/B][/COLOR]' % content)
        return

    tardis.log('========== listings download ==========')
    with open(dest, 'wb') as f:
        for chunk in r.iter_content(512):
            f.write(chunk)
        tardis.log('========= listings downloaded =========')
        return


def _pbhook(numblocks, blocksize, filesize, dp, start, range, url=None):
    try:
        percent = min(start+((numblocks*blocksize*range)/filesize), start+range)
        dp.update(int(percent))
    except Exception, e:
        tardis.log('%s Error Downloading Update' % str(e))
        percent = 100
        dp.update(int(percent))
    if dp.iscanceled(): 
        raise Exception('Canceled')



def doMain():
    if len(sys.argv) > 1:
        checkForUpdate(sys.argv[1])
    else:
        checkForUpdate(True) #silent


if __name__ == '__main__': 
    try:
        doMain()
    except:
        xbmcgui.Window(10000).clearProperty('TTV_UPDATE')
