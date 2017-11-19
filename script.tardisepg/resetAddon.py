#
#      Copyright (C) 2014 Richard Dean
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#

import xbmc
import xbmcaddon
import os

import sfile
import tardis
import settings

ttv     = xbmcaddon.Addon('script.tardis.tv')
ttvdata  = xbmc.translatePath(ttv.getAddonInfo('profile'))
epgdata  = tardis.PROFILE
hotkey   = xbmc.translatePath('special://profile/keymaps/ttv_hot.xml')

settingsFile = xbmc.translatePath(os.path.join(tardis.PROFILE, 'settings.cfg'))

def resetAddon():
    deleteFiles()
    tardis.SetSetting('epg.date', '2000-01-01')
    settings.set('ChannelsUpdated', 0, settingsFile)

    if tardis.isDSF():
        ttv.setSetting('SKIN', 'TTV-Skin')
        tardis.SetSetting('tardis.skin', 'EPG-Skin')
        tardis.SetSetting('playlist.url', '')

    tardis.CloseBusy()


def deleteFiles():
    try:
        sfile.rmtree(ttvdata)
        sfile.rmtree(epgdata)
        sfile.remove(hotkey)

        if tardis.isDSF():
            dsfdata = xbmc.translatePath(tardis.DSF.getAddonInfo('profile'))
            sfile.rmtree(dsfdata)
            tardis.DialogOK('GVAX TV successfully reset.', 'We will now quit the GVAX TV service.', 'Re-enter your details the next time you open the GVAX.TV App.')
            xbmc.executebuiltin('Quit')
        else:
        tardis.DialogOK('Tardis TV successfully reset.', 'It will be recreated next time', 'you start the guide.')

    except Exception, e:
        error = str(e)
        tardis.log('%s :: Error resetting TTV' % error)
        tardis.DialogOK('Tardis TV failed to reset.', error, 'Please restart Kodi and try again.')


if __name__ == '__main__':
    tardis.ShowBusy()
    resetAddon()
    ttv.setSetting('FIRSTRUN', 'false')
