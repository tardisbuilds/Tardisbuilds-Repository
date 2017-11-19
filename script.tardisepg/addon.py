import xbmc
import xbmcgui
import os
import tardis

def main():
    windowID = xbmcgui.Window(10000).getProperty('TTV_WINDOW')
    try:
        windowID = int(windowID)
        xbmc.executebuiltin('ActivateWindow(%d)' % windowID)
        return
    except:
        pass

    name   = tardis.TITLE + ' Launcher'
    script = os.path.join(tardis.HOME, 'launch.py')
    args   = ''
    cmd    = 'AlarmClock(%s,RunScript(%s,%s),%d,True)' % (name, script, args, 0)

    xbmc.executebuiltin('CancelAlarm(%s,True)' % name)
    xbmc.executebuiltin(cmd)


if __name__ == '__main__':
    try:    main()
    except: pass
