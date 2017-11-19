import xbmc
import xbmcaddon
import xbmcgui
import os
import re
import verify
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import base64
import cookielib
import pickle
import time
import datetime

import sfile

ADDONID     = 'script.tardisepg'
ADDON       =  xbmcaddon.Addon(ADDONID)
HOME        =  ADDON.getAddonInfo('path')
ICON        =  os.path.join(HOME, 'icon.png')
ICON        =  xbmc.translatePath(ICON)
PROFILE     =  xbmc.translatePath(ADDON.getAddonInfo('profile'))
RESOURCES   =  os.path.join(HOME, 'resources')
PVRACTIVE   = (xbmc.getCondVisibility('Pvr.HasTVChannels')) or (xbmc.getCondVisibility('Pvr.HasRadioChannels')) == True

try:
    TTV_ADDONID = 'script.tardis.tv'
    TTV_ADDON   =  xbmcaddon.Addon(TTV_ADDONID)
    TTV_HOME    =  xbmc.translatePath(TTV_ADDON.getAddonInfo('path'))
    TTV_PROFILE =  xbmc.translatePath(TTV_ADDON.getAddonInfo('profile'))
except: pass

resource    = base64.decodestring('aHR0cDovLzE2My4xNzIuNDYuMTIyL2ZpbGVzL2d1aWRlLw==')
baseurl     = base64.decodestring('aHR0cDovLzE2My4xNzIuNDYuMTIyL2ZpbGVzL2d1aWRlL3VwZGF0ZS8=')
loginurl    = base64.decodestring('aHR0cDovL3RhcmRpc2J1aWxkcy5jb20vd3AtbG9naW4ucGhw')
verifyurl   = base64.decodestring('aHR0cDovL3RhcmRpc2J1aWxkcy5jb20vd3AtbG9naW4ucGhw')

try:
    DSFID   =  ''
    DSF     =  xbmcaddon.Addon(DSFID)
    DSFVER  =  DSF.getAddonInfo('version')
except: pass


def SetSetting(param, value):
    value = str(value)

    if GetSetting(param) == value:
        return

    xbmcaddon.Addon(ADDONID).setSetting(param, value)


def GetSetting(param):
    return xbmcaddon.Addon(ADDONID).getSetting(param)


def GetXBMCVersion():
    version = xbmcaddon.Addon('xbmc.addon').getAddonInfo('version')
    version = version.split('.')
    return int(version[0]), int(version[1]) #major, minor eg, 13.9.902


MAJOR, MINOR = GetXBMCVersion()
FRODO        = (MAJOR == 12) and (MINOR < 9)

TARDISLOGOS  =  GetSetting('tardis.logo.folder')
SKIN        =  GetSetting('tardis.skin')
FILMON      =  GetSetting('FILMON')
VERSION     =  ADDON.getAddonInfo('version')
TITLE       = 'TardisEPG'
LOGOPACK    = 'Colour Logo Pack'
DEBUG       =  GetSetting('DEBUG') == 'true'
KEYMAP_HOT  = 'ttv_hot.xml'

CATCHUP     =  GetSetting('CATCHUP') == 'true'
ADULT       = 'Adultos'
SWISS       = 'Swisscom+IPTV'

datapath    = xbmc.translatePath(ADDON.getAddonInfo('profile'))
extras      = os.path.join(datapath, 'extras')
logos       = os.path.join(extras,   'logos')
cookiepath  = os.path.join(datapath, 'cookies')
cookiefile  = os.path.join(cookiepath, 'cookie')


def log(text):
    try:
        output = '%s V%s : %s' % (TITLE, VERSION, str(text))
        if DEBUG:
            xbmc.log(output)
        else:
            xbmc.log(output, xbmc.LOGDEBUG)
    except:
        pass


def getDSFVersion():
    try:
        version = int(DSFVER.replace('.', ''))
        return version
    except:
        version = 999
        return version


def isProtected():
    try:    return DSF.getSetting('PROTECTED') == 'true'
    except: return False

def isSwiss():
    try:    return DSF.getSetting('SWISSCOM') == 'true'
    except: return False

def isLimited():
    return xbmcgui.Window(10000).getProperty('DSF_LIMITED').lower() == 'true'


def getCategories():
    if isLimited():
        return ['Ni%C3%B1os']

    return GetSetting('categories').split('|')


def getCategoryList(path):
    import StringIO
    from xml.etree import ElementTree

    xml  = None
    cat  = dict()
    try:
        if sfile.exists(path):
            xml = sfile.read(path)
    except:
        pass

    if not xml:
        return {}

    xml = StringIO.StringIO(xml)
    xml = ElementTree.iterparse(xml, events=("start", "end"))

    for event, elem in xml:
        try:
            if event == 'end':
               if elem.tag == 'cats':
                   channel  = elem.findtext('channel')
                   category = elem.findtext('category')
                   if channel != '' and category != '':
                       cat[channel] = category
        except:
            pass

    return cat


def CloseBusy():
    try: xbmc.executebuiltin('Dialog.Close(busydialog)')
    except: pass

def ShowBusy():
    try: xbmc.executebuiltin('ActivateWindow(busydialog)')
    except: pass

    return None


def notify(message, length=5000):
    # CloseBusy()
    cmd = 'XBMC.notification(%s,%s,%d,%s)' % (TITLE, message, length, ICON)
    xbmc.executebuiltin(cmd)


def loadKeymap():
    try:
        file = 'zTTV_Keymap.xml'
        src  = os.path.join(HOME, 'resources', file)
        dst  = os.path.join('special://profile/keymaps', file)

        if not sfile.exists(dst):
            sfile.copy(src, dst)
            xbmc.sleep(1000)

        xbmc.executebuiltin('Action(reloadkeymaps)')
    except Exception, e:
        pass


def removeKeymap():
    try:
        file = 'zTTV_Keymap.xml'
        dst  = os.path.join('special://profile/keymaps', file)

        if sfile.exists(dst):
            sfile.remove(dst)
            xbmc.sleep(1000)

        xbmc.executebuiltin('Action(reloadkeymaps)')
    except Exception, e:
        pass


def patchSkins():
    skinPath = os.path.join(extras, 'skins')

    srcImage = os.path.join(RESOURCES, 'changer.png')
    srcFile  = os.path.join(RESOURCES, 'script-tvguide-changer.xml')

    current, dirs, files = sfile.walk(skinPath)

    for dir in dirs:
        dstImage = os.path.join(current, dir, 'resources', 'skins', 'Default', 'media', 'changer.png')
        dstFile  = os.path.join(current, dir, 'resources', 'skins', 'Default', '720p', 'script-tvguide-changer.xml')

        sfile.copy(srcImage, dstImage, overWrite=False)
        sfile.copy(srcFile,  dstFile,  overWrite=False)


def WriteKeymap(start, end, filename, cmd):
    filename = os.path.join('special://profile/keymaps', filename)
    theFile  = sfile.file(filename, 'w')
    cmd      = '\t\t\t<%s>%s</%s>\n'  % (start, cmd, end)

    theFile.write('<keymap>\n')
    theFile.write('\t<global>\n')
    theFile.write('\t\t<keyboard>\n')

    theFile.write(cmd)

    theFile.write('\t\t</keyboard>\n')
    theFile.write('\n')
    theFile.write('\t\t<remote>\n')

    theFile.write(cmd)

    theFile.write('\t\t</remote>\n')
    theFile.write('\t</global>\n')
    theFile.write('</keymap>\n')

    theFile.close()

    return True


def GetTardisUrl():
    if isDSF():
        if getSubSystem() == '80906':
            return baseurl + 'swi/'

        if getSubSystem() == '348821':
            return baseurl + 'spa/'

        if getSubSystem() == '809010':
            return baseurl + 'ita/'

    return baseurl + 'all/'


def getSubSystem():
    return DSF.getSetting('GVAX-SUBSYS')


def GetKey():
    if isDSF():
        return 'OTHER'

    return 'ALL CHANNELS'


def isDSF():
    if xbmc.getCondVisibility('System.HasAddon(%s)' % DSFID) == 1:
        log(DSFID)
        return True

    return False


def GetExtraUrl():
    return resource


def GetLoginUrl():
    return loginurl


def GetVerifyUrl():
    return verifyurl


def GetChannelType():
    return GetSetting('chan.type')


def GetChannelFolder():
    CUSTOM = '1'

    channelType = GetChannelType()

    if channelType == CUSTOM:
        path = GetSetting('user.chan.folder')
        MigrateChannels(path)
    else:
        path = datapath

    return path


def GetGMTOffset():
    offset = 0
    return datetime.timedelta(hours = offset)


def saveCookies(requests_cookiejar, filename):
    if not os.path.isfile(cookiefile):
        try: os.makedirs(cookiepath)
        except: pass

    with open(cookiefile, 'wb') as f:
        pickle.dump(requests_cookiejar, f)


def loadCookies(filename):
    if not os.path.isfile(cookiefile):
        try: os.makedirs(cookiepath)
        except: pass
        
        open(cookiefile, 'a').close()
        
    try:
        with open(cookiefile, 'rb') as f:
            return pickle.load(f)
    except: pass
        
    return ''


def resetCookies():
    try:
        if os.path.isfile(cookiefile):
            os.remove(cookiefile)
    except: pass


def BackupCats():
    currcat = os.path.join(PROFILE, 'cats.xml')
    bakcat  = os.path.join(PROFILE, 'cats-bak.xml')

    try:    sfile.copy(currcat, bakcat)
    except: pass


def MigrateChannels(dst):
    dst = os.path.join(dst, 'channels')
    src = os.path.join(datapath, 'channels')

    if not sfile.exists(dst):
        try:    sfile.copytree(src, dst)
        except: pass


def FirstRun():
    if GetUser() != '' and GetPass() != '':
        return True

    if not isDSF():
        if DialogYesNo('Would you like to choose from one of our Channel Line-ups?', 
                        'These are customised listings all set up to save you time.',
                        'You can change this later using Tardis TV Tools'):

            import extras

            URL      =  base64.decodestring('aHR0cDovLzE2My4xNzIuNDYuMTIyL2ZpbGVzL2d1aWRlLw==')
            baseurl  =  URL + 'lineups/'
            jsonurl  =  baseurl + 'lineups.json'
            response =  extras.getList(jsonurl, 'lineups', 'lineup')

            lineups  = []
            for result in response:
                label  = result['-name']
                url    = baseurl + result['-url']
                sfZip  = baseurl + result['-sfzip']
                isSF   = result['-sf']

                lineups.append((label, url, isSF, sfZip))

            menu = []
            for lineup in lineups:
                menu.append(lineup[0])

            title  = 'Please select a Channel Line-up'
            option =  xbmcgui.Dialog().select(title, menu)
            extras.installLineup(lineups[option])

    if DialogYesNo('Tardis TV requires a Login.', '', 'Would you like to enter your account details now?'):
        username = DialogKB('', 'Enter Your Tardis TV Username')
        if isDSF():
            xbmcaddon.Addon(DSFID).setSetting('username', username)
        else:
            SetSetting('username', username)

        password = DialogKB('', 'Enter Your Tardis TV Password')
        if isDSF():
            xbmcaddon.Addon(DSFID).setSetting('password', password)
        else:
            SetSetting('password', password)
        
    if verify.CheckCredentials():
        return True

    return False


def ShowSettings():
    ADDON.openSettings()


def getPreviousTime(setting):
    try:
        time_object = GetSetting(setting)
        previousTime = parseTime(time_object)
    
        return previousTime
    
    except:
        time_object  = '2001-01-01 00:00:00'
        previousTime = parseTime(time_object)
    
        return previousTime


def parseTime(when):
    if type(when) in [str, unicode]:
        dt = when.split(' ')
        d  = dt[0]
        t  = dt[1]
        ds = d.split('-')
        ts = t.split(':')
        when = datetime.datetime(int(ds[0]), int(ds[1]) ,int(ds[2]), int(ts[0]), int(ts[1]), int(ts[2].split('.')[0]))
        
    return when


def validTime(setting, maxAge):
    previousTime = getPreviousTime(setting)
    now          = datetime.datetime.today()
    delta        = now - previousTime
    nSeconds     = (delta.days * 86400) + delta.seconds
    
    return nSeconds <= maxAge


def validToRun(silent=False):
    #try:    count = int(GetSetting('LOGIN_COUNT'))
    #except: count = -1
    #
    #count += 1
    #
    #SetSetting('LOGIN_COUNT', str(count))
    #
    #if count % 3 == 0:
    #    return True

    setting      = 'LOGIN_TIME'
    previousTime = getPreviousTime(setting)
    now          = datetime.datetime.today()
    delta        = now - previousTime
    nSeconds     = (delta.days * 86400) + delta.seconds
    
    if nSeconds > 70 * 60:
        cmd = 'XBMC.RunScript(special://home/addons/script.tardisepg/getIni.py)'
        log('-------- TTV UPDATE INI FILES --------')
        xbmc.executebuiltin(cmd)

        if not doLogin(silent):
            return False

        SetSetting('LOGIN_TIME', str(now))

    return True


def doLogin(silent=False):
    log ('************ Tardis EPG Login ************')
    with requests.Session() as s:
        if not silent:
            message = 'Logging into Tardis TV'
            # notify(message)
            log(message)
        try:
            s.get(GetLoginUrl(), verify=False)
        except: 
            return False

        PAYLOAD  = { 'log' : GetUser(), 'pwd' : GetPass(), 'wp-submit' : 'Log In' }
        response = 'login_error'
        code     =  0
        
        if GetUser() and GetPass():
            login    = s.post(GetLoginUrl(), data=PAYLOAD, verify=False)
            response = login.content
            code     = login.status_code
            # saveCookies(s.cookies, cookiefile)
            log(code)
        if 'no-access-redirect' in response:
            error   = '301 - No Access.'
            message = 'It appears that your subscription has expired.'
            log(message + ' : ' + error)
            if not silent:
                DialogOK(message, error, 'Please check your account at www.tardisbuilds.com')
            return False
            
        areLost    = 'Are you lost' in response
        loginError = 'login_error' in response
        okay       =  (not areLost) and (not loginError)
        
        if okay:
            message = 'Logged into Tardis TV'
            log(message)
            # if not silent:
            #     notify(message)
            return True

        try:
            error = re.compile('<div id="login_error">(.+?)<br />').search(response).groups(1)[0]
            error = error.replace('<strong>',  '')
            error = error.replace('</strong>', '')
            error = error.replace('<a href="http://tardisbuild.com/wp-login.php?action=lostpassword">Lost your password?</a>', '')
            error = error.strip()
        except:
            error = ''
        
        message = 'There was a problem logging into Tardis TV.'
        log(message + ' : ' + error)
        if not silent:
            DialogOK(message, error, 'Please check your account at www.tardisbuilds.com')
        return False


def GetUser():
    if isDSF():
       username = xbmcaddon.Addon(DSFID).getSetting('username')
       return username

    username = GetSetting('username')

    return username
    

def GetPass():
    if isDSF():
       password = xbmcaddon.Addon(DSFID).getSetting('password')
       return password

    password = GetSetting('password')

    return password

    
def GetCats():
    path = os.path.join(PROFILE, 'cats.xml')


def GetChannels():
    path = os.path.join(PROFILE , 'chan.xml')

    return path
def selectMenu(title, menu):
    options = []
    for option in menu:
        options.append(option[0])

    option = xbmcgui.Dialog().select(title, options)

    if option < 0:
        return -1

    return menu[option][1]


def DialogOK(line1, line2='', line3=''):
    d = xbmcgui.Dialog()
    d.ok(TITLE + ' - ' + VERSION, line1, line2 , line3)


def DialogKB(value = '', heading = ''):
    kb = xbmc.Keyboard('', '')
    kb.setHeading(heading)
    kb.doModal()
    if (kb.isConfirmed()):
        value = kb.getText()
    return value


def DialogYesNo(line1, line2='', line3='', noLabel=None, yesLabel=None):
    d = xbmcgui.Dialog()
    if noLabel == None or yesLabel == None:
        return d.yesno(TITLE + ' - ' + VERSION, line1, line2 , line3) == True
    else:
        return d.yesno(TITLE + ' - ' + VERSION, line1, line2 , line3, noLabel, yesLabel) == True


def Progress(line1 = '', line2 = '', line3 = '', hide = False):
    dp = xbmcgui.DialogProgress()
    dp.create(TITLE, line1, line2, line3)
    dp.update(0)

    if hide:
        try:
            xbmc.sleep(250)
            WINDOW_PROGRESS = xbmcgui.Window(10101)
            CANCEL_BUTTON   = WINDOW_PROGRESS.getControl(10)
            CANCEL_BUTTON.setVisible(False)
        except:
            pass

    return dp


def openSettings(focus=None):
    addonID = ADDONID
    if not focus: 
        return xbmcaddon.Addon(addonID).openSettings()
    
    try:
        xbmc.executebuiltin('Addon.OpenSettings(%s)' % addonID)

        value1, value2 = str(focus).split('.')

        if FRODO:
            xbmc.executebuiltin('SetFocus(%d)' % (int(value1) + 200))
            xbmc.executebuiltin('SetFocus(%d)' % (int(value2) + 100))
        else:
            xbmc.executebuiltin('SetFocus(%d)' % (int(value1) + 100))
            xbmc.executebuiltin('SetFocus(%d)' % (int(value2) + 200))

    except Exception, e:
        log (str(e))
        return
