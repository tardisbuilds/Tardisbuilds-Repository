import xbmc,xbmcaddon,xbmcgui,xbmcplugin,urllib,urllib2,os,re,sys,shutil
import base64,time,datetime
from resources.lib.modules import checker
from resources.lib.modules import plugintools

addon_id            = 'plugin.video.tardis-fixtures'
AddonTitle          = '[COLOR blue]Tardis Fixtures[/COLOR]'
ADDON_PATH          = xbmc.translatePath('special://home/addons/' + addon_id)
icon                = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
fanart              = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
vs_icon             = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
CLEANER_FILE        = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'resources/files/cleaner.xml'))
SUPPORTED_ADDONS_FILE= xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'resources/files/supported_addons.xml'))
OPEN_MESSAGE        = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'resources/files/notice.txt'))

REPO_INFO           = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'resources/files/repository.txt'))
REPO_FOLDER         = xbmc.translatePath(os.path.join('special://home/addons/repository.Tardisrepo'))

BASE                = base64.decodestring('bm9uZQ==') 
SUPPORTED_ADDONS    = base64.decodestring('aHR0cDovLzE2My4xNzIuNDYuMTIyL2ZpbGVzL21hc3RlcmJldGEvZml4dHVyZXMvc3VwcG9ydGVkLnhtbA==') 
ADDON_NOTICE        = base64.decodestring('aHR0cDovLzE2My4xNzIuNDYuMTIyL2ZpbGVzL21hc3RlcmJldGEvZml4dHVyZXMvbWVzc2FnZS50eHQ=') 
CLEANER_URL         = base64.decodestring('aHR0cDovLzE2My4xNzIuNDYuMTIyL2ZpbGVzL21hc3RlcmJldGEvZml4dHVyZXMvY2xlYW5jaGFubmVscy50eHQ=') 
dialog              = xbmcgui.Dialog()
dp                  = xbmcgui.DialogProgress()
cachePath           = os.path.join(xbmc.translatePath('special://home'), 'cache')
tempPath            = os.path.join(xbmc.translatePath('special://home'), 'temp')

def GetMenu():

    message=open_url_no_replace(ADDON_NOTICE)
    if len(message)>1:
        comparefile = OPEN_MESSAGE
        r = open(comparefile)
        compfile = r.read()       
        if compfile == message:pass
        else:
            showText('[B][COLOR white]Find My Game Notice[/COLOR][/B]', message)
            text_file = open(comparefile, "w")
            text_file.write(message)
            text_file.close()

    today_raw = datetime.date.today()
    today_formated = datetime.datetime.strftime(today_raw,'%A %d %B %Y') 
    
    addDir('My Channel','url',8,icon,fanart)
    addDir('Live Scores - Todays Games','url',7,icon,fanart)
    if file == "online": addLink('Using built in Tardis Fixures INI files. - Click To Change','null',998,icon,fanart)
    else: addLink('Using local INI file. - Click To Change','null',998,icon,fanart)
    addLink('****************************************************************','',999,icon,fanart)
    addLink('[B][COLOR blue]Events - [/COLOR][/B]' + str(today_formated).upper() + '','',999,icon,fanart)

    get_date = datetime.datetime.now()
    url = base64.decodestring('aHR0cDovLzE2My4xNzIuNDYuMTIyL2ZpbGVzL21hc3RlcmJldGEvZml4dHVyZXMvZGF5cy8=')
    base = get_date.day

    today = base

    url = url + str(today) + '.xml'

    url2=url
    link=open_url(url)
    match= re.compile('<item>(.+?)</item>').findall(link)
    
    if match:
        for item in match:
            try:
                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                url = url2 + "!" + name
                try: 
                    event,name = name.split(')'); event = event.replace('(','')
                    name,time = name.split(' - ')
                    name = '[B][COLOR white]' + event + '[/COLOR][COLOR grey]' + name + '[/COLOR] - [COLOR blue]' + time + '[/B][/COLOR]'
                except:
                    try:
                        name,time = name.split(' - ')
                        name = '[B][COLOR white]' + name + '[/COLOR] - [COLOR blue]' + time + '[/B][/COLOR]'
                    except:
                        name = '[B][COLOR white]' + name + '[/B][/COLOR]'
                addDir(name,url,2,vs_icon,fanart)
            except: pass

def Get_INI_Data(name,url,iconimage):

    try:
        url,DISPLAY_NAME = url.split('!')
    except: 
        dialog.ok(AddonTitle, "[COLOR white]Sorry there was a problem processing your request.[/COLOR]","[COLOR blue]Please Check Custom ini File[/COLOR]")
        quit()

    termlist=[]

    link=open_url(url)
    urls=re.compile('<title>'+re.escape(DISPLAY_NAME)+'</title>(.+?)</item>',re.DOTALL).findall(link)[0]
    links=re.compile('<search>(.+?)</search>').findall(urls)
    for sturl in links:
        termlist.append( sturl )

    dp.create(AddonTitle,"[COLOR blue]Just Seaching through your add-ons for streams[/COLOR]",'[COLOR yellow]Please wait...[/COLOR]','')    
    dp.update(0)

    namelist=[]
    urllist=[]
    markerlist=[]
    dp.update(0)
        
    if file == "online":
        content = open_url_no_replace(base64.decodestring('aHR0cDovLzE2My4xNzIuNDYuMTIyL2ZpbGVzL21hc3RlcmJldGEvZml4dHVyZXMvYWRkb25zLmluaQ=='))
        content = content.replace('\r', '')
        content = content.split('\n')
        for line in content:

            try:
                if "[plugin" in line:
                    id = line.replace("[","").replace("]","")
                else:
                    a = line.split('=')[0]
                    b = str(a)
                    c = b + '='
                    d = str(line)
                    e = d.replace(c,'')
                    b = b.strip()
                    e = e.strip()
                    f = line.split('=')[0]
                    namelist.append(b)
                    urllist.append(id + "SPLIT" + e)
                    markerlist.append(f)
                    combinedlists = list(zip(namelist,urllist,markerlist))
            except: pass

        content = open_url_no_replace(base64.decodestring('aHR0cDovLzE2My4xNzIuNDYuMTIyL2ZpbGVzL21hc3RlcmJldGEvZml4dHVyZXMvYWRkb25zX3N0cmVhbXMuaW5p'))
        content = content.replace('\r', '')
        content = content.split('\n')
        for line in content:

            try:
                if "[plugin" in line:
                    id = line.replace("[","").replace("]","")
                else:
                    a = line.split('=')[0]
                    b = str(a)
                    c = b + '='
                    d = str(line)
                    e = d.replace(c,'')
                    b = b.strip()
                    e = e.strip()
                    f = "Channel Stream"
                    namelist.append(b)
                    urllist.append(id + "SPLIT" + e)
                    markerlist.append(f)
                    combinedlists = list(zip(namelist,urllist,markerlist))
            except: pass
    else:
        f = open(file,mode='r'); content = f.read(); f.close()
        content = content.replace('\r', '')
        content = content.split('\n')
        for line in content:
            try:
                if "[plugin" in line:
                    id = line.replace("[","").replace("]","")
                else:
                    a = line.split('=')[0]
                    b = str(a)
                    c = b + '='
                    d = str(line)
                    e = d.replace(c,'')
                    b = b.strip()
                    e = e.strip()
                    f = "Custom INI"
                    namelist.append(b)
                    urllist.append(id + "SPLIT" + e)
                    markerlist.append(f)
                    combinedlists = list(zip(namelist,urllist,markerlist))
            except: pass

    tup = sorted(combinedlists)
    term_tup = sorted(termlist)

    dp.update(100)

    finalcountlist=[]
    finalnamelist=[]
    finalurllist=[]
    finaliconlist=[]
    finalfanartlist=[]
    aa = 0
    ab = 0

    for term in term_tup:
        for name,url,marker in tup:
            try:
                id,url = url.split("SPLIT")
                check_me = name
                name = name.replace("|PAID|","")
                name = CLEAN_NAME(name)
                if term.lower() in name.lower():
                    aa = aa + 1
                    show = name
                    addon_is = xbmc.translatePath('special://home/addons/' + id)
                    if os.path.exists (addon_is):
                        ab = ab + 1
                        iconimage = xbmc.translatePath(os.path.join('special://home/addons/' + id , 'icon.png'))
                        fanarts = xbmc.translatePath(os.path.join('special://home/addons/' + id , 'fanart.jpg'))
                        if "|PAID|" in check_me:
                            finalcountlist.append("3")
                            name = GET_NAME(id)
                            name = name + " - Subscription Addon"
                            title = "[COLOR dodgerblue][B]" + name + '[/B][/COLOR] - [COLOR blue]' + marker + "[/COLOR]"
                        else:
                            finalcountlist.append("2")      
                            name = GET_NAME(id)  
                            title = "[COLOR white][B]" + name + '[/B][/COLOR] - [COLOR blue]' + marker + "[/COLOR]"
                        finalnamelist.append(title)         
                        finalurllist.append(url)
                        finaliconlist.append(iconimage)         
                        finalfanartlist.append(fanarts)
                    else:
                        if "|PAID|" in check_me:
                            finalcountlist.append("0")
                            name = GET_NAME(id)
                            name = name + " - Subscription Addon"
                        else:
                            finalcountlist.append("1")      
                            name = GET_NAME(id)
                        title = '[COLOR darkgray]' + name + ' - ' + marker + ' | Addon Not Installed[/COLOR]'
                        finalnamelist.append(title)         
                        finalurllist.append(url)
                        finaliconlist.append(icon)     
                        finalfanartlist.append(fanart)
                    finalcombinedlists = list(zip(finalcountlist,finalnamelist,finalurllist,finaliconlist,finalfanartlist))
            except: pass
    checkerlist = []
    
    ac = 0

    addLink("[COLOR blue][B]We found " + str(aa) + " links, you have the addons to play " + str(ab) + " of those links.[/B][/COLOR]","url",999,icon,fanart)                
    addLink(">>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<","url",999,icon,fanart)               

    try:
        final_tup = sorted(finalcombinedlists, key=lambda x: int(x[0]),reverse=True)
        final_tup = sorted(final_tup,reverse=True)
        for count,name,url,iconimage,fanarts in final_tup:
            #if url not in str(checkerlist):
            ac = ac + 1
            checkerlist.append(url)     
            if "NOT INSTALLED" not in name.upper():
                addLink("[COLOR lightblue][B]Link " + str(ac) + ": [/B][/COLOR]" + name,url,3,iconimage,fanarts)
            else:
                addLink(name,url,999,iconimage,fanarts)

        dp.close()
    except:
        dp.close()
        dialog.ok(AddonTitle, "Sorry, no links were found.","[COLOR blue]For more results Tardis Fixtures Recomends adding more Add-ons [/COLOR]")
        quit()

def GET_NAME(string):

    f = open(SUPPORTED_ADDONS_FILE,mode='r'); msg = f.read(); f.close()
    msg = msg.replace('\n','')
    match= re.compile('<item>(.+?)</item>').findall(msg)
    found = 0
    for item in match:

        plugin=re.compile('<plugin>(.+?)</plugin>').findall(item)[0]
        display=re.compile('<name>(.+?)</name>').findall(item)[0]

        if string == plugin:
            found = 1
            name = display
    
    if found == 0:
        name = string
    
    return name

def PLAYER(name,url,iconimage):

    liz = xbmcgui.ListItem(name,iconImage=icon, thumbnailImage=icon)
    liz.setPath(url)
    xbmc.Player ().play(url, liz, False)
    quit()

def CLEAN_NAME(string):

    found = 0
    f = open(CLEANER_FILE,mode='r'); msg = f.read(); f.close()
    msg = msg.replace('\n','')
    match= re.compile('<item>(.+?)</item>').findall(msg)
    for item in match:
        OLD=re.compile('<old>(.+?)</old>').findall(item)[0]
        NEW=re.compile('<new>(.+?)</new>').findall(item)[0]
        OLD = OLD.lower()
        NEW = NEW.lower()
        string = string.lower()
        if OLD.lower() in string.lower():
            found = 1
            string = string.replace(OLD,NEW)
            string = string.title()
        if found == 1:
            return string
    
    return string

def SUPPORTED_ADDONS_LIST():

    addLink("[COLOR white][B]Tardis Fixtures - Supported Addons[/B][/COLOR]",'',999,icon,fanart)
    addLink("#####################################",'',999,icon,fanart)

    pluginlist  = []
    displaylist = []
    contactlist = []
    sourcelist = []
    urllist     = []
    countlist   = []

    f = open(SUPPORTED_ADDONS_FILE,mode='r'); msg = f.read(); f.close()
    msg = msg.replace('\n','')
    match= re.compile('<item>(.+?)</item>').findall(msg)
    for item in sorted(match):
        plugin=re.compile('<plugin>(.+?)</plugin>').findall(item)[0]
        display=re.compile('<name>(.+?)</name>').findall(item)[0]
        contact=re.compile('<dev>(.+?)</dev>').findall(item)[0]
        source_url=re.compile('<source>(.+?)</source>').findall(item)[0]
        url = display + '|SPLIT|' + plugin + '|SPLIT|' + contact + '|SPLIT|' + source_url

        addon_is = xbmc.translatePath('special://home/addons/' + plugin)
        if os.path.exists (addon_is):
            if "|PAID|" in contact:
                count = "3"
            else: count = "2"
        else: 
            if not "|PAID|" in contact:
                count = "1"
            else: count = "0"
        pluginlist.append(plugin)           
        displaylist.append(display)
        contactlist.append(contact)     
        sourcelist.append(source_url)                   
        urllist.append(url)
        countlist.append(count)
        combinedlists = list(zip(countlist,pluginlist,displaylist,contactlist,sourcelist,urllist))
                
    tup = sorted(combinedlists, key=lambda x: int(x[0]),reverse=True)
    for count,plugin,display,contact,source,url in tup:
        addon_is = xbmc.translatePath('special://home/addons/' + plugin)
        try:
            if os.path.exists (addon_is):
                iconimage = xbmc.translatePath(os.path.join('special://home/addons/' + plugin , 'icon.png'))
                fanarts = xbmc.translatePath(os.path.join('special://home/addons/' + plugin , 'fanart.jpg'))
                url = url + '|SPLIT|1'
                addLink("[COLOR lightblue][B]" + display + " - INSTALLED [/B][/COLOR]",url,999,iconimage,fanarts)
            else:
                url = url + '|SPLIT|0'
                addLink("[COLOR darkgray]" + display + " - NOT INSTALLED [/COLOR]",url,999,icon,fanart)
        except: pass
        
def SUPPORTED_ADDONS_DIALOG(url):
    
    paid = "null"
    try:
        name,url,contact,source,count,paid = url.split('|SPLIT|')
    except:
        name,url,contact,source,count = url.split('|SPLIT|')
        
    if paid != "null":
        contact = contact.replace("|PAID|","")
    
    dialog.ok(AddonTitle, "You can contact the developer of " + name + " on:", "[COLOR blue]" + contact + "[/COLOR]","[B][COLOR blue]Install Source: " + source + "[/COLOR][/B]")
    
    if count == "1":
        choice = xbmcgui.Dialog().yesno(AddonTitle, '[COLOR white]Would you like to launch ' + name + ' now?[/COLOR]','',yeslabel='[COLOR lime]YES[/COLOR]',nolabel='[COLOR blue]NO[/COLOR]')
        if choice == 1:
            xbmc.executebuiltin('ActivateWindow(10025,plugin://' + url + ')')
    else:
        choice = xbmcgui.Dialog().yesno(AddonTitle,"[B][COLOR blue]Install Source: " + source + "[/COLOR][/B]",'[COLOR white]' + name + ' is not installed. If the addon is available for download in any repository currently installed on your system we can attempt to install the addon. Would you like us to try and install ' + name + '?[/COLOR]','',yeslabel='[COLOR lime]YES[/COLOR]',nolabel='[COLOR blue]NO[/COLOR]')
        if choice == 1:
            xbmc.executebuiltin('ActivateWindow(10025,plugin://' + url + ')')

def GET_LIVE_SCORES(name,url,iconimage):
    
    team1list = []
    team2list = []
    scorelist = []
    minutelist = []
    markerlist = []

    link=open_url('http://www.livescores.com')
    match= re.compile('<div class="cal">(.+?)<div id="fb-root">').findall(link)
    string = str(match)
    match2= re.compile('<div class="min(.+?)data-esd="').findall(string)
    for item in match2:
        team1=re.compile('<div class="ply tright name">(.+?)</div>').findall(item)[0]
        team2=re.compile('<div class="ply name">(.+?)<').findall(item)[0]
        try:
            score=re.compile('class="scorelink">(.+?)</a>').findall(item)[0]
        except:
            score=re.compile('<div class="sco">(.+?)</div>').findall(item)[0]
        try:
            time=re.compile('"><img src=".+?" alt="live"/>(.+?)</div>').findall(item)[0]
        except: time=re.compile('">(.+?)</div>').findall(item)[0]
        time = time.replace('&#x27;',' Minute'); time = time.split('<')[0]
        
        if "minute" in time.lower():
            markerlist.append('4')
        elif "ht" in time.lower():
            markerlist.append('3')
        elif "ft" in time.lower():
            markerlist.append('2')
        elif "aet" in time.lower():
            markerlist.append('2')
        else: markerlist.append('1')

        team1list.append(team1)         
        team2list.append(team2) 
        scorelist.append(score)
        minutelist.append(time)
        combinedlists = list(zip(markerlist,team1list,team2list,scorelist,minutelist))
        
    tup = sorted(combinedlists, key=lambda x: int(x[0]),reverse=True)
    live = 0
    fulltime = 0
    later = 0
    for final_marker, team_1, team_2, score_, minute_ in tup:
        if final_marker == "4":
            if live == 0:
                addLink('[COLOR white][B]Live Now[/B][/COLOR]','url',999,icon,fanart)
                live = 1
        elif final_marker == "2":
            if fulltime == 0:
                addLink('[COLOR white][B]Finished[/B][/COLOR]','url',999,icon,fanart)
                fulltime = 1
        elif final_marker == "1":
            if later == 0:
                addLink('[COLOR white][B]Later Today[/B][/COLOR]','url',999,icon,fanart)
                later = 1
        minute_ = minute_.replace("'","").replace(' Minute',"'")
        score_ = score_.replace(" ","")
        addLink('[COLOR orangered][B]' + minute_ + "[/COLOR]- [COLOR dodgerblue]" + score_ + "[/COLOR][/B] | [COLOR white]" + team_1 + "vs" + team_2 + '[/COLOR]','url',999,icon,fanart)

def addDir(name,url,mode,iconimage,fanartimage):

    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanartimage="+urllib.quote_plus(fanartimage)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    liz.setProperty( "fanart_Image", fanartimage )
    liz.setProperty( "icon_Image", iconimage )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok

def addLink(name,url,mode,iconimage,fanartimage):

    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+iconimage+"&fanartimage="+urllib.quote_plus(fanartimage)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    liz.setProperty( "fanart_Image", fanartimage )
    liz.setProperty( "icon_Image", iconimage )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
    return ok

def showText(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(500)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
        try:
            xbmc.sleep(10)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            return
        except:
            pass

def open_url(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', base64.decodestring('V2FyZG9jdG9yUm9ja3M='))
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    link=link.replace('\n','').replace('\r','').replace('<fanart></fanart>','<fanart>x</fanart>').replace('<thumbnail></thumbnail>','<thumbnail>x</thumbnail>').replace('<utube>','<link>https://www.youtube.com/watch?v=').replace('</utube>','</link>')#.replace('></','>x</')
    return link

def open_url_no_replace(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', base64.decodestring('V2FyZG9jdG9yUm9ja3M='))
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

def channels():
    
    addLink("[COLOR aqua][B]Search for your Sports Channel[/B][/COLOR]",'',999,icon,fanart)
    addLink("#####################################",'',999,icon,fanart)
    addDir('[COLOR white][B]UK Freeveiw[/B][/COLOR]','url',14,icon,fanart)
    addDir('[COLOR white][B]UK Sports[/B][/COLOR]','url',9,icon,fanart)
    addDir('[COLOR white][B]US & Canada[/B][/COLOR]','url',10,icon,fanart)
    addDir('[COLOR white][B]International[/B][/COLOR]','url',11,icon,fanart)
    addDir('[COLOR white][B]Club Channels[/B][/COLOR]','url',12,icon,fanart)
def UK():			
    url = base64.decodestring('aHR0cDovLzE2My4xNzIuNDYuMTIyL2ZpbGVzL21hc3RlcmJldGEvZml4dHVyZXMvY2hhbm5lbHMv')

    url = url + 'uk.xml'

    url2=url
    link=open_url(url)
    match= re.compile('<item>(.+?)</item>').findall(link)
    
    if match:
        for item in match:
            try:
                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                url = url2 + "!" + name
                try: 
                    event,name = name.split(')'); event = event.replace('(','')
                    name,time = name.split(' - ')
                    name = '[B][COLOR dodgerblue]' + event + '[/COLOR][COLOR white]' + name + '[/COLOR] - [COLOR blue]' + time + '[/B][/COLOR]'
                except:
                    try:
                        name,time = name.split(' - ')
                        name = '[B][COLOR white]' + name + '[/COLOR] - [COLOR blue]' + time + '[/B][/COLOR]'
                    except:
                        name = '[B][COLOR white]' + name + '[/B][/COLOR]'
                addDir(name,url,2,vs_icon,fanart)
            except: pass
def US():			
    url = base64.decodestring('aHR0cDovLzE2My4xNzIuNDYuMTIyL2ZpbGVzL21hc3RlcmJldGEvZml4dHVyZXMvY2hhbm5lbHMv')

    url = url + 'us.xml'

    url2=url
    link=open_url(url)
    match= re.compile('<item>(.+?)</item>').findall(link)
    
    if match:
        for item in match:
            try:
                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                url = url2 + "!" + name
                try: 
                    event,name = name.split(')'); event = event.replace('(','')
                    name,time = name.split(' - ')
                    name = '[B][COLOR dodgerblue]' + event + '[/COLOR][COLOR white]' + name + '[/COLOR] - [COLOR blue]' + time + '[/B][/COLOR]'
                except:
                    try:
                        name,time = name.split(' - ')
                        name = '[B][COLOR white]' + name + '[/COLOR] - [COLOR blue]' + time + '[/B][/COLOR]'
                    except:
                        name = '[B][COLOR white]' + name + '[/B][/COLOR]'
                addDir(name,url,2,vs_icon,fanart)
            except: pass
def INT():			
    url = base64.decodestring('aHR0cDovLzE2My4xNzIuNDYuMTIyL2ZpbGVzL21hc3RlcmJldGEvZml4dHVyZXMvY2hhbm5lbHMv')

    url = url + 'int.xml'

    url2=url
    link=open_url(url)
    match= re.compile('<item>(.+?)</item>').findall(link)
    
    if match:
        for item in match:
            try:
                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                url = url2 + "!" + name
                try: 
                    event,name = name.split(')'); event = event.replace('(','')
                    name,time = name.split(' - ')
                    name = '[B][COLOR dodgerblue]' + event + '[/COLOR][COLOR white]' + name + '[/COLOR] - [COLOR blue]' + time + '[/B][/COLOR]'
                except:
                    try:
                        name,time = name.split(' - ')
                        name = '[B][COLOR white]' + name + '[/COLOR] - [COLOR blue]' + time + '[/B][/COLOR]'
                    except:
                        name = '[B][COLOR white]' + name + '[/B][/COLOR]'
                addDir(name,url,2,vs_icon,fanart)
            except: pass
def Club():			
    url = base64.decodestring('aHR0cDovLzE2My4xNzIuNDYuMTIyL2ZpbGVzL21hc3RlcmJldGEvZml4dHVyZXMvY2hhbm5lbHMv')

    url = url + 'club.xml'

    url2=url
    link=open_url(url)
    match= re.compile('<item>(.+?)</item>').findall(link)
    
    if match:
        for item in match:
            try:
                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                url = url2 + "!" + name
                try: 
                    event,name = name.split(')'); event = event.replace('(','')
                    name,time = name.split(' - ')
                    name = '[B][COLOR dodgerblue]' + event + '[/COLOR][COLOR white]' + name + '[/COLOR] - [COLOR blue]' + time + '[/B][/COLOR]'
                except:
                    try:
                        name,time = name.split(' - ')
                        name = '[B][COLOR white]' + name + '[/COLOR] - [COLOR blue]' + time + '[/B][/COLOR]'
                    except:
                        name = '[B][COLOR white]' + name + '[/B][/COLOR]'
                addDir(name,url,2,vs_icon,fanart)
            except: pass

def Freeview():			
    url = base64.decodestring('aHR0cDovLzE2My4xNzIuNDYuMTIyL2ZpbGVzL21hc3RlcmJldGEvZml4dHVyZXMvY2hhbm5lbHMv')

    url = url + 'freev.xml'

    url2=url
    link=open_url(url)
    match= re.compile('<item>(.+?)</item>').findall(link)
    
    if match:
        for item in match:
            try:
                name=re.compile('<title>(.+?)</title>').findall(item)[0]
                url = url2 + "!" + name
                try: 
                    event,name = name.split(')'); event = event.replace('(','')
                    name,time = name.split(' - ')
                    name = '[B][COLOR dodgerblue]' + event + '[/COLOR][COLOR white]' + name + '[/COLOR] - [COLOR blue]' + time + '[/B][/COLOR]'
                except:
                    try:
                        name,time = name.split(' - ')
                        name = '[B][COLOR white]' + name + '[/COLOR] - [COLOR blue]' + time + '[/B][/COLOR]'
                    except:
                        name = '[B][COLOR white]' + name + '[/B][/COLOR]'
                addDir(name,url,2,vs_icon,fanart)
            except: pass

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                               
        return param

type = plugintools.get_setting("addons.ini.type")
file = plugintools.get_setting("addons.ini.file")
if type != "0":
    file = xbmc.translatePath(file)
else: file = "online"
if file == "":
    file = "online"
SEND_TO_CHECK = REPO_FOLDER + '|SPLIT|' + REPO_INFO
checker.check(SEND_TO_CHECK)

if not os.path.isfile(SUPPORTED_ADDONS_FILE):
    f = open(SUPPORTED_ADDONS_FILE,'w')

if not os.path.isfile(OPEN_MESSAGE):
    f = open(OPEN_MESSAGE,'w')

if not os.path.isfile(CLEANER_FILE):
    f = open(CLEANER_FILE,'w')

supported=open_url_no_replace(SUPPORTED_ADDONS)
if len(supported)>1:
    comparefile = SUPPORTED_ADDONS_FILE
    r = open(comparefile)
    compfile = r.read()       
    if compfile == supported:pass
    else:
        text_file = open(comparefile, "w")
        text_file.write(supported)
        text_file.close()
        
supported=open_url_no_replace(CLEANER_URL)
if len(supported)>1:
    comparefile = CLEANER_FILE
    r = open(comparefile)
    compfile = r.read()       
    if compfile == supported:pass
    else:
        text_file = open(comparefile, "w")
        text_file.write(supported)
        text_file.close()

params=get_params(); name=None; url=None; mode=None; iconimage=None; fanartimage=None
try: name=urllib.unquote_plus(params["name"])
except: pass
try: url=urllib.unquote_plus(params["url"])
except: pass
try: mode=int(params["mode"])
except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
try: fanartimage=urllib.quote_plus(params["fanartimage"])
except: pass

if mode==None or url==None or len(url)<1: GetMenu()
elif mode==1:Get_Content(name,url,iconimage)
elif mode==2:Get_INI_Data(name,url,iconimage)
elif mode==3:PLAYER(name,url,iconimage)
elif mode==4:SUPPORTED_ADDONS_LIST()
elif mode==5:SUPPORTED_ADDONS_DIALOG(url)
elif mode==7:GET_LIVE_SCORES(name,url,iconimage)
elif mode==8:channels()
elif mode==9:UK()
elif mode==10:US()
elif mode==11:INT()
elif mode==12:Club()
elif mode==14:Freeview()
elif mode==998:xbmcaddon.Addon(id=addon_id).openSettings()

xbmcplugin.endOfDirectory(int(sys.argv[1]))