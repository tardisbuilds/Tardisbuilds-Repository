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
import os

import tardis
import sfile

hotkey = xbmc.translatePath('special://profile/keymaps/zTTV_toggle.xml')


def resetHotkey():
    deleteFiles()


def deleteFiles():
    try:
        sfile.remove(hotkey)
        xbmc.executebuiltin('Action(reloadkeymaps)')
        tardis.DialogOK('Tardis TV Hot Key successfully reset.', '', 'Thank you.')

    except Exception, e:
        error = str(e)
        tardis.log('%s :: Error resetting TTV' % error)
        tardis.DialogOK('Tardis TV Hot Key failed to reset.', error, 'Please restart Kodi and try again.')

resetHotkey()
