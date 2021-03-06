# -*- coding: utf-8 -*-
"""
    default.py --- Missy Addon entry point
    Copyright (C) 2017, Wardoctor, Midraal

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import __builtin__
import os
import sys

import koding
import koding.router as router
import resources.lib.search
import resources.lib.sources
import resources.lib.testings
import resources.lib.util.info
import xbmc
import xbmcaddon
import xbmcplugin
from koding import route
from resources.lib.util.xml import MissyList, display_list
import resources.lib.util.views
import resources.lib.sports


addon_id = xbmcaddon.Addon().getAddonInfo('id')
addon_name = xbmcaddon.Addon().getAddonInfo('name')
home_folder = xbmc.translatePath('special://home/')
addon_folder = os.path.join(home_folder, 'addons')
art_path = os.path.join(addon_folder, addon_id)
content_type = "files"


@route("main")
def root():
    """root menu of the addon"""
    base = "http://163.172.46.122/files/missy/main.txt"
    if not get_list(base):
        koding.Add_Dir(
            name="Message",
            url="Sorry, server is down",
            mode="message",
            folder=True,
            icon=xbmcaddon.Addon().getAddonInfo("icon"),
            fanart=xbmcaddon.Addon().getAddonInfo("fanart"),
            content_type="")
        koding.Add_Dir(
            name="Search",
            url="",
            mode="Search",
            folder=True,
            icon=xbmcaddon.Addon().getAddonInfo("icon"),
            fanart=xbmcaddon.Addon().getAddonInfo("fanart"),
            content_type="")
        koding.Add_Dir(
            name="Testings",
            url='{"file_name":"testings.xml"}',
            mode="Testings",
            folder=True,
            icon=xbmcaddon.Addon().getAddonInfo("icon"),
            fanart=xbmcaddon.Addon().getAddonInfo("fanart"),
            content_type="")


@route(mode='get_list_uncached', args=["url"])
def get_list_uncached(url):
    """display missy list uncached"""
    global content_type
    missy_list = MissyList(url, cached=False)
    if not missy_list:
        koding.dolog("returned empty for " + url)
    items = missy_list.get_list()
    content = missy_list.get_content_type()
    if items == []:
        return False
    if content:
        content_type = content
    display_list(items, content_type)
    return True


@route(mode="get_list", args=["url"])
def get_list(url):
    """display missy list"""
    global content_type
    missy_list = MissyList(url)
    if not missy_list:
        koding.dolog("returned empty for " + url)
    items = missy_list.get_list()
    content = missy_list.get_content_type()
    if items == []:
        return False
    if content:
        content_type = content
    display_list(items, content_type)
    return True


@route(mode="all_episodes", args=["url"])
def all_episodes(url):
    global content_type
    import pickle
    import xbmcgui
    season_urls = pickle.loads(url)
    result_items = []
    dialog = xbmcgui.DialogProgress()
    dialog.create(addon_name, "Loading items")
    num_urls = len(season_urls)
    for index, season_url in enumerate(season_urls):
        if dialog.iscanceled():
            break
        percent = ((index + 1) * 100) / num_urls
        dialog.update(percent, "processing lists", "%s of %s" % (index + 1,
                                                                 num_urls))

        missy_list = MissyList(season_url)
        result_items.extend(missy_list.get_list(skip_dialog=True))
    content_type = "episodes"
    display_list(result_items, "episodes")


@route(mode="Settings")
def settings():
    xbmcaddon.Addon().openSettings()


@route(mode="ScraperSettings")
def scraper_settings():
    xbmcaddon.Addon('script.module.nanscrapers').openSettings()


@route(mode="ResolverSettings")
def resolver_settings():
    xbmcaddon.Addon('script.module.urlresolver').openSettings()


@route(mode="message", args=["url"])
def show_message(message):
    import xbmcgui
    if len(message) > 80:
        koding.Text_Box(addon_name, message)
    else:
        xbmcgui.Dialog().ok(addon_name, message)


@route('clearCache')
def clear_cache():
    import xbmcgui
    dialog = xbmcgui.Dialog()
    if dialog.yesno(addon_name, "Clear Metadata?"):
        koding.Remove_Table("meta")
        koding.Remove_Table("episode_meta")
    if dialog.yesno(addon_name, "Clear XML cache?"):
        koding.Remove_Table("xml_cache")
    if dialog.yesno(addon_name, "Clear Scraper Cache?"):
        import nanscrapers
        nanscrapers.clear_cache()
    if dialog.yesno(addon_name, "Clear GIF Cache?"):
        dest_folder = os.path.join(
            xbmc.translatePath(xbmcaddon.Addon().getSetting("cache_folder")),
            "artcache")
        koding.Delete_Folders(dest_folder)


def get_addon_url(mode, url=""):
    import urllib
    result = sys.argv[0] + "?mode=%s" % mode

    if url:
        result += "&url=%s" % urllib.quote_plus(url)
    return result


def first_run_wizard():
    import xbmcgui
    addon = xbmcaddon.Addon()

    #  LocalWords:  clearCache

    #  LocalWords:  artcache
    dialog = xbmcgui.Dialog()
    addon.setSetting("first_run", "false")
    if not dialog.yesno(addon_name, "Run Setup Wizard?"):
        return
    if dialog.yesno(
            addon_name,
            "choose movie metadata provider",
            nolabel="TMDB",
            yeslabel="TRAKT"):
        addon.setSetting("movie_metadata_provider", "Trakt")
    else:
        addon.setSetting("movie_metadata_provider", "TMDB")

    if dialog.yesno(
            addon_name,
            "choose tv metadata provider",
            nolabel="TVDB",
            yeslabel="TRAKT"):
        addon.setSetting("tv_metadata_provider", "Trakt")
    else:
        addon.setSetting("tv_metadata_provider", "TVDB")

    if dialog.yesno(
            addon_name,
            "choose Selector type",
            nolabel="HD/SD",
            yeslabel="Link Selector"):
        addon.setSetting("use_link_dialog", "true")
    else:
        default_links = ["BOTH", "HD", "SD"]
        selected = dialog.select("choose default link", default_links)
        if selected != -1:
            addon.setSetting("default_link", default_links[selected])

    themes = [
        "DEFAULT", "CARS", "COLOURFUL", "KIDS", "MOVIES", "SPACE",
        "GIF LIFE", "GIF NATURE", "USER"
    ]
    selected = dialog.select("choose theme", themes)
    if selected != -1:
        addon.setSetting("theme", themes[selected])

    if dialog.yesno(addon_name, "Enable GIF support?\n"
                    "May cause issues on lower end devices"):
        addon.setSetting("enable_gifs", "true")
    else:
        addon.setSetting("enable_gifs", "false")


# koding.User_Info()
if xbmcaddon.Addon().getSetting("first_run") == "true":
    first_run_wizard()

__builtin__.MISSY_BASE_DOMAIN = "163.172.46.122"

foldername = xbmc.getInfoLabel("Container.FolderName")
if foldername in ["", "plugin.program.super.favourites"]:
    __builtin__.MISSY_WIDGET = True
else:
    __builtin__.MISSY_WIDGET = False

router.Run()

xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=False)
if not xbmcaddon.Addon().getSetting("first_run") == "true":
    if content_type == "files":
        content_type = "other"
    resources.lib.util.views.set_list_view_mode(content_type)
