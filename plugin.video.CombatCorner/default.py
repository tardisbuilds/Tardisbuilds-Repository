# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Youtube Channel
# (c) 2015 - Simple TechNerd
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.CombatCorner'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')


channellist=[
        ("UFC", "user/UFC", 'https://yt3.ggpht.com/-QeD1gcM_f7k/AAAAAAAAAAI/AAAAAAAAAAA/RrU6oF2FBU0/s900-c-k-no-rj-c0xffffff/photo.jpg'),
        ("UFC On Fox", "user/UFCONFOXofficial", 'https://yt3.ggpht.com/-lj8-zSzRk4E/AAAAAAAAAAI/AAAAAAAAAAA/7PEm8PTojB8/s900-c-k-no-rj-c0xffffff/photo.jpg'),
        ("MMA Fighting on SBN", "user/MMAFightingonSBN", 'https://yt3.ggpht.com/-sp-vOJ7qPYY/AAAAAAAAAAI/AAAAAAAAAAA/FSCMv-tTC90/s900-c-k-no-rj-c0xffffff/photo.jpg'),
        ("AXS TV Fights", "channel/UCYsccWrD_6uRxWq3_L8ZWRA", 'https://yt3.ggpht.com/-ABqQE8cdd8k/AAAAAAAAAAI/AAAAAAAAAAA/B54qTSFUbWI/s900-c-k-no-rj-c0xffffff/photo.jpg'),
        ("Fight UK MMA", "user/FightUKMMA", 'https://yt3.ggpht.com/-wwZRRRJ1UqQ/AAAAAAAAAAI/AAAAAAAAAAA/TrfLk98wOtw/s900-c-k-no-rj-c0xffffff/photo.jpg'),
        ("MAX Muay Thai Official", "user/maxmuaythaichannel/videos", 'https://yt3.ggpht.com/-a9BdqMWD7Rs/AAAAAAAAAAI/AAAAAAAAAAA/liusnGeW-_U/s900-c-k-no-rj-c0xffffff/photo.jpg'),
        ("Tiger Muay Thai", "user/NakMuayThai", 'https://yt3.ggpht.com/-8iIZaT3PtGA/AAAAAAAAAAI/AAAAAAAAAAA/b1HqGsrAYA0/s900-c-k-no-rj-c0xffffff/photo.jpg'),
        ("HBO Boxing", "user/HBOsports", 'https://yt3.ggpht.com/-xspd8uYupTc/AAAAAAAAAAI/AAAAAAAAAAA/UTwanzEE9iM/s900-c-k-no-rj-c0xffffff/photo.jpg'),
        ("Boxing Legends TV", "channel/UCuHeVY3bLH1OdhhQ_KyJnUA", 'https://yt3.ggpht.com/-WyimirILAOk/AAAAAAAAAAI/AAAAAAAAAAA/Ku3F1M8diyY/s900-c-k-no-rj-c0xffffff/photo.jpg'),
        ("Premier Boxing Champions", "channel/UCWXYAGB9SadlL6p5Bb66wWw", 'https://yt3.ggpht.com/-O3WOfE_rWaE/AAAAAAAAAAI/AAAAAAAAAAA/TAaWn7fnYqc/s900-c-k-no-rj-c0xffffff/photo.jpg'),
        ("iFL TV", "user/iFilmLdnProductions", 'https://yt3.ggpht.com/-aBdJXeua6zE/AAAAAAAAAAI/AAAAAAAAAAA/HmMwEVyz1cg/s900-c-k-no-rj-c0xffffff/photo.jpg'),
        ("Fighthub", "user/fighthub", 'https://yt3.ggpht.com/-oa41B6PXzW4/AAAAAAAAAAI/AAAAAAAAAAA/ftSzlIb416I/s900-c-k-no-rj-c0xffffff/photo.jpg'),
        ("Boxing Channel", "user/theboxingchanneltv", 'https://yt3.ggpht.com/-bzAVWRTWacI/AAAAAAAAAAI/AAAAAAAAAAA/605U856VjJA/s900-c-k-no-rj-c0xffffff/photo.jpg'),
 ]



# Entry point
def run():
    plugintools.log("youtubeAddon.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("youtubeAddon.main_list "+repr(params))

for name, id, icon in channellist:
	plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,folder=True )



run()