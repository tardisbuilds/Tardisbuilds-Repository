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

addonID = 'plugin.video.HuntersHideout'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')


channellist=[
        ("Hushin", "user/hushinwithlavere", 'https://yt3.ggpht.com/-JpsZ1CeUQEo/AAAAAAAAAAI/AAAAAAAAAAA/5ycDthsjCcs/s900-c-k-no-rj-c0xffffff/photo.jpg'),
        ("Big Game Hunting New Zealand", "user/BGHNZ", 'https://yt3.ggpht.com/-4aRZlGYAsJQ/AAAAAAAAAAI/AAAAAAAAAAA/E9LnBwA18Kg/s900-c-k-no-rj-c0xffffff/photo.jpg'),
        ("Freelance Duck Hunting", "channel/UC8tonlQAEqFdqa2Z7tEr2xA", 'https://yt3.ggpht.com/-q-VMvTGvnDE/AAAAAAAAAAI/AAAAAAAAAAA/QDJ-9KxZo7k/s900-c-k-no-rj-c0xffffff/photo.jpg'),				
        ("Irinea Sea", "channel/UC__Xy4l5O3Gr_aCLF3-nHZQ", 'https://yt3.ggpht.com/-CJbfl7SaIfk/AAAAAAAAAAI/AAAAAAAAAAA/655EdIHtfXE/s900-c-k-no-rj-c0xffffff/photo.jpg'),				
        ("Gunsmoke Guns TV", "user/GunsmokeGunsTV", 'https://yt3.ggpht.com/-ruoo5AS_NCo/AAAAAAAAAAI/AAAAAAAAAAA/HCLrvek9oCA/s900-c-k-no-rj-c0xffffff/photo.jpg'),				
        ("Coles World", "channel/UCizOl-2KteunfY2NrLH_Bfg", 'https://yt3.ggpht.com/-jTYsboandX0/AAAAAAAAAAI/AAAAAAAAAAA/HsaOD3F8ax0/s900-c-k-no-rj-c0xffffff/photo.jpg'),				
        ("Gun Time with Brandon", "user/Brandon401401", 'https://yt3.ggpht.com/-W9jQbtzmCos/AAAAAAAAAAI/AAAAAAAAAAA/5o-UhxqR9Wk/s900-c-k-no-rj-c0xffffff/photo.jpg'),				
		("Air Arms Hunting SA", "user/MoshDubber", 'https://yt3.ggpht.com/-rMOovrqXnro/AAAAAAAAAAI/AAAAAAAAAAA/j-g0spoaUfU/s900-c-k-no-rj-c0xffffff/photo.jpg'),				
		("Hunters Vermin", "user/HuntersVermin", 'https://yt3.ggpht.com/-UCQvG4zxMaQ/AAAAAAAAAAI/AAAAAAAAAAA/-uh5tIFhdCs/s900-c-k-no-rj-c0xffffff/photo.jpg'),				
		("Solo Hunter", "user/huntnhouse", 'https://yt3.ggpht.com/-2F6dWZeUvK0/AAAAAAAAAAI/AAAAAAAAAAA/0EAp_714UHE/s900-c-k-no-rj-c0xffffff/photo.jpg'),				
		("Squirrel Hunter", "user/squirrelhuntertv", 'https://yt3.ggpht.com/--C_kGVGn9XE/AAAAAAAAAAI/AAAAAAAAAAA/DOBycBMCOAM/s900-c-k-no-rj-c0xffffff/photo.jpg'),				
		("Team Wild TV", "user/TeamWildHunting", 'https://yt3.ggpht.com/-zlScCAXRxgU/AAAAAAAAAAI/AAAAAAAAAAA/9GyuTM2Jcpk/s900-c-k-no-rj-c0xffffff/photo.jpg'),				
		("English Shooting", "user/EnglishShooting", 'https://yt3.ggpht.com/-hm8lFbZelBY/AAAAAAAAAAI/AAAAAAAAAAA/NiXwyDaxUDY/s900-c-k-no-rj-c0xffffff/photo.jpg'),				
		("Shooting Stuff Australia", "channel/UC93Vc7br01HAjES5ywVBXrg", 'https://yt3.ggpht.com/-4ZWFNq51XFc/AAAAAAAAAAI/AAAAAAAAAAA/b39isQZs9pY/s900-c-k-no-rj-c0xffffff/photo.jpg'),				
		("314299 Shooting Channel", "user/314299", 'https://yt3.ggpht.com/-VV8mE5g8JqM/AAAAAAAAAAI/AAAAAAAAAAA/3gEMju97Tg8/s900-c-k-no-rj-c0xffffff/photo.jpg'),				
		("We Like Shooting", "user/WeLikeShootingVideos", 'https://yt3.ggpht.com/-BEkCQoIayGU/AAAAAAAAAAI/AAAAAAAAAAA/dPHI2p_6H6U/s900-c-k-no-rj-c0xffffff/photo.jpg'),				
		("Kirsten Joy Weiss", "user/KirstenJoyWeiss", 'https://yt3.ggpht.com/-lNCAoU3eyD4/AAAAAAAAAAI/AAAAAAAAAAA/xi8WP_nt8RE/s900-c-k-no-rj-c0xffffff/photo.jpg'),				
		("Vermin Hunters TV", "user/VerminHuntersTV", 'https://yt3.ggpht.com/-o95mxkQbyCc/AAAAAAAAAAI/AAAAAAAAAAA/r10YO6bcwAA/s900-c-k-no-rj-c0xffffff/photo.jpg'),				
		("The Shooting Show", "user/theshootingshow", 'https://yt3.ggpht.com/-8YbCKkvGqqA/AAAAAAAAAAI/AAAAAAAAAAA/yHsxj2PR6VE/s900-c-k-no-rj-c0xffffff/photo.jpg'),				
		("Fieldsports", "user/fieldsportschannel", 'https://yt3.ggpht.com/-mhyYPklAIls/AAAAAAAAAAI/AAAAAAAAAAA/ZMF2bL5nubc/s900-c-k-no-rj-c0xffffff/photo.jpg'),				
		("Hunting Gear Guy", "user/HGGTheHuntingGearGuy", 'https://yt3.ggpht.com/-9yWqDnTkFnU/AAAAAAAAAAI/AAAAAAAAAAA/tR2RrN6SbcM/s900-c-k-no-rj-c0xffffff/photo.jpg'),				
		("Hunting/Fishing TV", "channel/UCqXJkjCTWrbMaFt6OxIz4Mw", 'https://yt3.ggpht.com/-ohpwoorVH94/AAAAAAAAAAI/AAAAAAAAAAA/4mWd10EIykE/s900-c-k-no-rj-c0xffffff/photo.jpg'),				
		("Keith Warren", "user/OutdoorAdventures", 'https://yt3.ggpht.com/-KSpSC_3QpwM/AAAAAAAAAAI/AAAAAAAAAAA/B9og2QNtZ5w/s900-c-k-no-rj-c0xffffff/photo.jpg'),				
		("Hunters Hub", "user/extremeKhunting", 'https://yt3.ggpht.com/-EzjJQMlAA4Y/AAAAAAAAAAI/AAAAAAAAAAA/aHwzYfXbJTE/s900-c-k-no-rj-c0xffffff/photo.jpg'),				
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