from urllib import quote

from xbmcswift2 import Plugin

CHANNEL_LIST = {
    1: ("BBC One", "http://tvcatchup.com/watch/bbcone"),
    2: ("BBC Two", "http://tvcatchup.com/watch/bbctwo"),
    3: ("ITV", "http://tvcatchup.com/watch/itv"),
    4: ("Channel 4", "http://tvcatchup.com/watch/channel4"),
    5: ("Channel 5", "http://tvcatchup.com/watch/channel5"),
    17: ("BBC News", "http://tvcatchup.com/watch/bbcnews"),
    18: ("CBBC", "http://tvcatchup.com/watch/cbbc"),
    24: ("CBeebies", "http://tvcatchup.com/watch/cbeebies"),
    12: ("BBC3", "http://tvcatchup.com/watch/bbc3"),
    13: ("BBC4", "http://tvcatchup.com/watch/bbc4"),
    501: ("MillenniumTV", "http://tvcatchup.com/watch/millenniumtv"),
    73: ("Quest", "http://tvcatchup.com/watch/quest"),
    37: ("VIVA", "http://tvcatchup.com/watch/viva"),
    31: ("BBC Parliament", "http://tvcatchup.com/watch/bbcparliament"),
    78: ("RT", "http://tvcatchup.com/watch/rt"),
    65: ("BBC Red Button", "http://tvcatchup.com/watch/bbcredbutton"),
    95: ("Gala TV", "http://tvcatchup.com/watch/galatv"),
    151: ("Sail TV", "http://tvcatchup.com/watch/sailtv"),
    177: ("Sub TV", "http://tvcatchup.com/watch/subtv"),
    158: ("Community Channel", "http://tvcatchup.com/watch/communitychannel"),
    144: ("S4C", "http://tvcatchup.com/watch/s4c"),
	205: ("TV Warehouse", "http://tvcatchup.com/watch/tvwarehouse"),
	33: ("QVC", "http://tvcatchup.com/watch/qvc"),
	185: ("QVC Beauty", "http://tvcatchup.com/watch/qvcbeauty"),
	186: ("QVC Extra", "http://tvcatchup.com/watch/qvcextra"),
	187: ("QVC Style", "http://tvcatchup.com/watch/qvcstyle"),
	50: ("Al Jazeera", "http://tvcatchup.com/watch/aljazeera"),
	146: ("CCTV News", "http://tvcatchup.com/watch/cctv-news"),
	154: ("Ideal World", "http://tvcatchup.com/watch/ideal-world"),
	155: ("Ideal Extra", "http://tvcatchup.com/watch/ideal-extra"),
	156: ("Create and Craft", "http://tvcatchup.com/watch/create-and-craft"),
	157: ("Craft Extra", "http://tvcatchup.com/watch/craft-extra")
#	211: ("BBC Olympics 1", "http://tvcatchup.com/watch/bbcolympics1"),
#	212: ("BBC Olympics 2", "http://tvcatchup.com/watch/bbcolympics2"),
#	213: ("BBC Olympics 3", "http://tvcatchup.com/watch/bbcolympics3"),
#	214: ("BBC Olympics 4", "http://tvcatchup.com/watch/bbcolympics4"),
#	215: ("BBC Olympics 5", "http://tvcatchup.com/watch/bbcolympics5"),
#	216: ("BBC Olympics 6", "http://tvcatchup.com/watch/bbcolympics6"),
#	217: ("BBC Olympics 7", "http://tvcatchup.com/watch/bbcolympics7"),
#	218: ("BBC Olympics 8", "http://tvcatchup.com/watch/bbcolympics8")
}

plugin = Plugin()


@plugin.route('/')
def index():
    return [{'label': info[0],
             'path': "plugin://plugin.video.livestreamer/play?url={0}".format(quote(info[1])),
             'is_playable': True,
             'thumbnail': 'http://tvcatchup.com/tvc-static//images/channels/v3/{0}.png'.format(cid)}
            for cid, info in CHANNEL_LIST.items()]

if __name__ == '__main__':
    plugin.run()
