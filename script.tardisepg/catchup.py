# coding: UTF-8
import sys
l1llll11_opy_ = sys.version_info [0] == 2
l1ll11l_opy_ = 2048
l1ll11_opy_ = 7
def l111l1_opy_ (ll_opy_):
	global l1ll1_opy_
	l1111l1_opy_ = ord (ll_opy_ [-1])
	l1llll1_opy_ = ll_opy_ [:-1]
	l1l11_opy_ = l1111l1_opy_ % len (l1llll1_opy_)
	l11ll_opy_ = l1llll1_opy_ [:l1l11_opy_] + l1llll1_opy_ [l1l11_opy_:]
	if l1llll11_opy_:
		l1l1ll1_opy_ = unicode () .join ([unichr (ord (char) - l1ll11l_opy_ - (l11l1l_opy_ + l1111l1_opy_) % l1ll11_opy_) for l11l1l_opy_, char in enumerate (l11ll_opy_)])
	else:
		l1l1ll1_opy_ = str () .join ([chr (ord (char) - l1ll11l_opy_ - (l11l1l_opy_ + l1111l1_opy_) % l1ll11_opy_) for l11l1l_opy_, char in enumerate (l11ll_opy_)])
	return eval (l1l1ll1_opy_)
import xbmc
import xbmcgui
import xbmcaddon
import tardis
import urllib2
import re
import json
import os
import datetime
from hashlib import md5
from threading import Timer
global l11lll1_opy_, l1l1ll_opy_, l11l11_opy_, l1lll1ll_opy_
l11lll1_opy_  = None
l1l1ll_opy_  = False
l11l11_opy_ = 0
l1lll1ll_opy_ = 0
ADDON = tardis.ADDON
HOME  = ADDON.getAddonInfo(l111l1_opy_ (u"ࠫࡵࡧࡴࡩࠩࠀ"))
ICON  = os.path.join(HOME, l111l1_opy_ (u"ࠬ࡯ࡣࡰࡰ࠱ࡴࡳ࡭ࠧࠁ"))
ICON  = xbmc.translatePath(ICON)
TITLE = tardis.TITLE
SETTING = l111l1_opy_ (u"࠭ࡌࡐࡉࡌࡒࡤࡎࡄࡕࡘࠪࠂ")
l1l11l1_opy_           = 'http://www.filmon.tv/'
l1llll_opy_       =  l1l11l1_opy_ + l111l1_opy_ (u"ࠨࡣࡳ࡭࠴࡯࡮ࡪࡶ࠲ࠫࠄ")
l11_opy_      =  l1l11l1_opy_ + l111l1_opy_ (u"ࠩࡤࡴ࡮࠵࡬ࡰࡩ࡬ࡲࡄࡹࡥࡴࡵ࡬ࡳࡳࡥ࡫ࡦࡻࡀࠩࡸࠬ࡬ࡰࡩ࡬ࡲࡂࠫࡳࠧࡲࡤࡷࡸࡽ࡯ࡳࡦࡀࠩࡸ࠭ࠅ")
l1l1l_opy_     =  l1l11l1_opy_ + l111l1_opy_ (u"ࠪࡥࡵ࡯࠯࡭ࡱࡪࡳࡺࡺ࠿ࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡭ࡨࡽࡂࠫࡳࠨࠆ")
l11ll1_opy_     =  l1l11l1_opy_ + l111l1_opy_ (u"ࠫࡦࡶࡩ࠰ࡦࡹࡶ࠲ࡧࡤࡥࡁࡶࡩࡸࡹࡩࡰࡰࡢ࡯ࡪࡿ࠽ࠦࡵࠩࡧ࡭ࡧ࡮࡯ࡧ࡯ࡣ࡮ࡪ࠽ࠦࡵࠩࡴࡷࡵࡧࡳࡣࡰࡱࡪࡥࡩࡥ࠿ࠨࡷࠫࡹࡴࡢࡴࡷࡣࡹ࡯࡭ࡦ࠿ࠨࡷࠬࠇ")
l11l111_opy_ =  l1l11l1_opy_ + l111l1_opy_ (u"ࠬࡧࡰࡪ࠱ࡧࡺࡷ࠳࡬ࡪࡵࡷࡃࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡱࡥࡺ࠿ࠨࡷࠬࠈ")
l1l1l11_opy_     =  l1l11l1_opy_ + l111l1_opy_ (u"࠭ࡡࡱ࡫࠲ࡨࡻࡸ࠭ࡳࡧࡰࡳࡻ࡫࠿ࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡭ࡨࡽࡂࠫࡳࠧࡴࡨࡧࡴࡸࡤࡪࡰࡪࡣ࡮ࡪ࠽ࠦࡵࠪࠉ")
l11l11l_opy_      =  l1l11l1_opy_ + l111l1_opy_ (u"ࠧࡵࡸ࠲ࡥࡵ࡯࠯ࡵࡸࡪࡹ࡮ࡪࡥ࠰ࠧࡶࡃࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡱࡥࡺ࠿ࠨࡷࠬࠊ")
l1l11l_opy_ = 275
l1lll1l_opy_  = l111l1_opy_ (u"ࠨࠩࠋ")
l11ll1l_opy_  = l111l1_opy_ (u"ࠩࠪࠌ")
AVAILABLE = False
if not AVAILABLE:
    try:
        l11111_opy_    = xbmcaddon.Addon(l111l1_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡉ࠲࡙࠴ࡖࠨࠍ"))
        l1lll1l_opy_ = l11111_opy_.getSetting(l111l1_opy_ (u"ࠫ࡫࡯࡬࡮ࡱࡱࡣࡺࡹࡥࡳࠩࠎ"))
        l11ll1l_opy_ = l11111_opy_.getSetting(l111l1_opy_ (u"ࠬ࡬ࡩ࡭࡯ࡲࡲࡤࡶࡡࡴࡵࠪࠏ"))
        l11ll1l_opy_ = md5(l11ll1l_opy_).hexdigest()
        AVAILABLE = len(l1lll1l_opy_) > 0 and len(l11ll1l_opy_) > 0
    except:
        AVAILABLE = False
if not AVAILABLE:
    try:
        l11111_opy_    = xbmcaddon.Addon(l111l1_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡩࡳࡦࡺࡳࡥࡹࡺࡶࠨࠐ"))
        l1lll1l_opy_ = l11111_opy_.getSetting(l111l1_opy_ (u"ࠧࡶࡵࡨࡶࠬࠑ"))
        l11ll1l_opy_ = l11111_opy_.getSetting(l111l1_opy_ (u"ࠨࡲࡤࡷࡸ࠭ࠒ"))
        l11ll1l_opy_ = md5(l11ll1l_opy_).hexdigest()
        AVAILABLE = len(l1lll1l_opy_) > 0 and len(l11ll1l_opy_) > 0
    except:
        AVAILABLE = False
tardis.log(l111l1_opy_ (u"ࠩࡉ࡭ࡱࡳ࡯࡯ࠢࡘࡷࡪࡸ࡮ࡢ࡯ࡨࠤ࠿ࠦࠥࡴࠩࠓ") % l1lll1l_opy_)
tardis.log(l111l1_opy_ (u"ࠪࡊ࡮ࡲ࡭ࡰࡰࠣࡔࡦࡹࡳࡸࡱࡵࡨࠥࡀࠠࠦࡵࠪࠔ") % l11ll1l_opy_)
if AVAILABLE:
    tardis.log(l111l1_opy_ (u"ࠫࡋ࡯࡬࡮ࡱࡱࠤ࡮ࡹࠠࡂࡘࡄࡍࡑࡇࡂࡍࡇࠪࠕ"))
else:
    tardis.log(l111l1_opy_ (u"ࠬࡌࡩ࡭࡯ࡲࡲࠥ࡯ࡳࠡࡐࡒࡘࠥࡇࡖࡂࡋࡏࡅࡇࡒࡅࠨࠖ"))
def notify(message, length=5000):
    cmd = l111l1_opy_ (u"࠭ࡘࡃࡏࡆ࠲ࡳࡵࡴࡪࡨ࡬ࡧࡦࡺࡩࡰࡰࠫࠩࡸ࠲ࠥࡴ࠮ࠨࡨ࠱ࠫࡳࠪࠩࠗ") % (TITLE, message, length, ICON)
    xbmc.executebuiltin(cmd)
def l11l1l1_opy_():
    return l111l1_opy_ (u"ࠧࠡࡏࡲࡾ࡮ࡲ࡬ࡢ࠱࠸࠲࠵ࠦࠨࡘ࡫ࡱࡨࡴࡽࡳ࠼ࠢࡘ࠿ࠥ࡝ࡩ࡯ࡦࡲࡻࡸࠦࡎࡕࠢ࠸࠲࠶ࡁࠠࡦࡰ࠰ࡋࡇࡁࠠࡳࡸ࠽࠵࠳࠿࠮࠱࠰࠶࠭ࠥࡍࡥࡤ࡭ࡲ࠳࠷࠶࠰࠹࠲࠼࠶࠹࠷࠷ࠡࡈ࡬ࡶࡪ࡬࡯ࡹ࠱࠶࠲࠵࠴࠳ࠨ࠘")
def isValid(stream):
    if stream.startswith(l111l1_opy_ (u"ࠨࡊࡇࡘ࡛࠭࠙")):
        return True
    if stream.startswith(l111l1_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠼࠲࠳ࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡼࡱ࠭ࠚ")):
        return True
    if not AVAILABLE:
        return False
    if stream.startswith(l111l1_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠽࠳࠴ࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡋ࠴ࡔ࠯ࡘࠪࠛ")):
        return True
    if stream.startswith(l111l1_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠾࠴࠵ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡩࡳࡦࡺࡳࡥࡹࡺࡶࠨࠜ")):
        return True
    return False
def l1ll1l1_opy_(url):
    global l1lll1ll_opy_
    try:
        req  = urllib2.Request(url)
        req.add_header(l111l1_opy_ (u"࡛ࠬࡳࡦࡴ࠰ࡅ࡬࡫࡮ࡵࠩࠝ"), l11l1l1_opy_())
        resp = urllib2.urlopen(req, timeout=10)
        headers = resp.headers
        gmt     = headers[l111l1_opy_ (u"࠭ࡄࡢࡶࡨࠫࠞ")].split(l111l1_opy_ (u"ࠧ࠭ࠢࠪࠟ"))[-1]
        gmt     = datetime.datetime.strptime(gmt, l111l1_opy_ (u"ࠨࠧࡧࠤࠪࡨ࡛ࠠࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠥࡍࡍࡕࠩࠠ"))
        l1lll1ll_opy_ = gmt - datetime.datetime.today()
        l1lll1ll_opy_ = ((l1lll1ll_opy_.days * 86400) + (l1lll1ll_opy_.seconds + 1800)) / 3600
        l1lll1ll_opy_ *= -3600
        l111l11_opy_ = resp.read()
        resp.close()
        return l111l11_opy_
    except Exception, e:
        tardis.log(l111l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡌ࡫ࡴࡉࡖࡐࡐ࠱ࠦࡵࡳ࡮ࠣࡁࠥࠫࡳࠨࠡ") % url)
        tardis.log(str(e))
        return str(e)
def l111ll_opy_():
    if (not l1lll1l_opy_) or (not l11ll1l_opy_):
        return
    l111111_opy_()
    try:
        global l11l11_opy_
        l11l11_opy_ = 0
        response  = l1ll1l1_opy_(l1llll_opy_)
        l11l11_opy_ = re.compile(l111l1_opy_ (u"ࠪࠦࡸ࡫ࡳࡴ࡫ࡲࡲࡤࡱࡥࡺࠤ࠽ࠦ࠭࠴ࠫࡀࠫࠥࠫࠢ")).search(response).group(1)
    except:
        pass
def l1llll1l_opy_():
    tardis.log(l111l1_opy_ (u"ࠫࡊࡴࡴࡦࡴ࡬ࡲ࡬ࠦ࡬ࡰࡩ࡬ࡲࠬࠣ"))
    global l11lll1_opy_, l1l1ll_opy_, l11l11_opy_
    l1l1ll_opy_ = False
    if l11l11_opy_ == 0:
        l111ll_opy_()
    url   = l11_opy_ % (l11l11_opy_, l1lll1l_opy_, l11ll1l_opy_)
    l1llll1l_opy_ = l1ll1l1_opy_(url)
    l1l1ll_opy_ = l111l1_opy_ (u"ࠬࡋࡒࡓࡑࡕࠫࠤ") not in l1llll1l_opy_.upper()
    if l1l1ll_opy_:
        message = l111l1_opy_ (u"࠭ࡌࡰࡩࡪࡩࡩࠦࡩ࡯ࡶࡲࠤࡋ࡯࡬࡮ࡱࡱࠫࠥ")
    else:
        message = l111l1_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡐࡴ࡭ࠠࡪࡰࡷࡳࠥࡌࡩ࡭࡯ࡲࡲࠬࠦ")
    tardis.log(message)
    notify(message)
    if l1l1ll_opy_:
        l11lll1_opy_ = Timer(l1l11l_opy_, l1l111l_opy_)
        l11lll1_opy_.start()
def l111111_opy_():
    global l11lll1_opy_
    if l11lll1_opy_:
        l11lll1_opy_.cancel()
        del l11lll1_opy_
        l11lll1_opy_ = None
def l1l111l_opy_():
    l111111_opy_()
    global l1l1ll_opy_, l11l11_opy_
    if not l1l1ll_opy_:
        return
    id = l11l11_opy_
    l1l1ll_opy_  = False
    l11l11_opy_ = 0
    try:
        url    = l1l1l_opy_ % id
        l1l111l_opy_ = l1ll1l1_opy_(url)
        l1l1lll_opy_  = json.loads(l1l111l_opy_)
        if l111l1_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩࠧ") in l1l1lll_opy_:
            l1l1ll_opy_ = not l1l1lll_opy_[l111l1_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪࠨ")]
        if l1l1ll_opy_:
            tardis.log(l111l1_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡌࡰࡩࡲࡹࡹࠦ࡯ࡧࠢࡉ࡭ࡱࡳ࡯࡯ࠩࠩ"))
        else:
            tardis.log(l111l1_opy_ (u"ࠫࡑࡵࡧࡨࡧࡧࠤࡴࡻࡴࠡࡱࡩࠤࡋ࡯࡬࡮ࡱࡱࠫࠪ"))
    except:
        pass
def l11l_opy_(l1l111_opy_):
    global l1lll1ll_opy_
    start   = datetime.datetime(1970, 1, 1)
    l111_opy_   = l1l111_opy_ - start
    seconds = (l111_opy_.days * 86400) + l111_opy_.seconds
    return seconds - l1lll1ll_opy_
def l1lllll_opy_(channel):
    global l11l11_opy_
    try:
        if l11l11_opy_ == 0:
            return None
        l1lll1l1_opy_ = l1ll1l1_opy_(l11l11l_opy_ % (channel, l11l11_opy_))
        return l1lll1l1_opy_
    except Exception, e:
        tardis.log(l111l1_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡬࡫ࡴࡈࡷ࡬ࡨࡪࠦࠥࡴࠩࠫ") % str(e))
        return None
def l1l1l1l_opy_(l1l1l1_opy_):
    try:
        return int(re.compile(l111l1_opy_ (u"࠭ࡵࡳ࡮ࡀࠬ࠳࠱࠿ࠪࠨࠪࠬ")).search(l1l1l1_opy_).group(1))
    except:
        pass
    try:
        l11ll11_opy_ = l1l1l1_opy_.rsplit(l111l1_opy_ (u"ࠧࡤࡪࡢࡪࡦࡴࡡࡳࡶࡀࠫ࠭"), 1)[-1]
        l11ll11_opy_ = int(l11ll11_opy_.split(l111l1_opy_ (u"ࠨ࠾ࡁࠫ࠮"), 1)[0])
        return l11ll11_opy_
    except:
        return None
def getProgram(channel, start):
    tardis.log(l111l1_opy_ (u"ࠩࡈࡲࡹ࡫ࡲࡪࡰࡪࠤ࡬࡫ࡴࡑࡴࡲ࡫ࡷࡧ࡭ࠨ࠯"))
    tardis.log(l111l1_opy_ (u"ࠪࡇ࡭ࡧ࡮࡯ࡧ࡯ࠤࡂࠦࠥࡴࠩ࠰") % str(channel))
    tardis.log(l111l1_opy_ (u"ࠫࡘࡺࡡࡳࡶࠣࠤࠥࡃࠠࠦࡵࠪ࠱") % str(start))
    try:
        l1lll_opy_ = l11l_opy_(start)
        tardis.log(l111l1_opy_ (u"࡙ࠬࡴࡢࡴࡷࡘࡘࠦ࠽ࠡࠧࡶࠫ࠲") % str(l1lll_opy_))
        tardis.log(l111l1_opy_ (u"࠭ࡴࡺࡲࡨࠬࡘࡺࡡࡳࡶࡗࡗ࠮ࠦ࠽ࠡࠧࡶࠫ࠳") % type(l1lll_opy_))
        l1lll1l1_opy_ = l1lllll_opy_(channel)
        if not l1lll1l1_opy_:
            return None
        l1lll1l1_opy_ = json.loads(l1lll1l1_opy_)
        for l1lll11_opy_ in l1lll1l1_opy_:
            tardis.log(l111l1_opy_ (u"ࠧࡠࡡࡢࡣࡤࡥ࡟ࡠࡡࡢࡣࡤࡥ࡟ࡠࡡࡢࡣࡤࡥ࡟ࡠࡡࡢࡣࡤࡥ࡟ࡠࡡࠪ࠴"))
            tardis.log(l111l1_opy_ (u"ࠨࡖࡼࡴࡪࠦ࠽ࠡࠧࡶࠫ࠵") % type(l1lll11_opy_))
            tardis.log(l111l1_opy_ (u"ࠩࡗࡽࡵ࡫ࠠࡰࡨࠣࡴࡷࡵࡧࡳࡣࡰ࡟ࡸࡺࡡࡳࡶࡧࡥࡹ࡫ࡴࡪ࡯ࡨࡡࠥࡃࠠࠦࡵࠪ࠶") % type(l1lll11_opy_[l111l1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡦࡤࡸࡪࡺࡩ࡮ࡧࠪ࠷")]))
            tardis.log(l1lll11_opy_)
            tardis.log(l111l1_opy_ (u"ࠫࡤࡥ࡟ࡠࡡࡢࡣࡤࡥ࡟ࡠࡡࡢࡣࡤࡥ࡟ࡠࡡࡢࡣࡤࡥ࡟ࡠࡡࡢࡣࡤࡥࠧ࠸"))
            tardis.log(l111l1_opy_ (u"ࠬ࠷ࠠࠡࠢࠪ࠹"))
            tardis.log(l111l1_opy_ (u"࠭࠲ࠡࠢࠣࠫ࠺"))
            tardis.log(l111l1_opy_ (u"ࠧ࠴ࠢࠣࠤࠬ࠻"))
            if l111l1_opy_ (u"ࠨࡵࡷࡥࡷࡺࡤࡢࡶࡨࡸ࡮ࡳࡥࠨ࠼") in l1lll11_opy_ and l111l1_opy_ (u"ࠩࡳࡶࡴ࡭ࡲࡢ࡯ࡰࡩࠬ࠽") in l1lll11_opy_:
                if int(l1lll11_opy_[l111l1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡦࡤࡸࡪࡺࡩ࡮ࡧࠪ࠾")]) == l1lll_opy_:
                    return l1lll11_opy_[l111l1_opy_ (u"ࠫࡵࡸ࡯ࡨࡴࡤࡱࡲ࡫ࠧ࠿")]
    except Exception, e:
        tardis.log(l111l1_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡬࡫ࡴࡑࡴࡲ࡫ࡷࡧ࡭ࠡࠧࡶࠫࡀ") % str(e))
    tardis.log(l111l1_opy_ (u"࠭ࡒࡦࡶࡸࡶࡳ࡯࡮ࡨࠢࡑࡳࡳ࡫ࠠࡧࡴࡲࡱࠥ࡭ࡥࡵࡒࡵࡳ࡬ࡸࡡ࡮ࠩࡁ"))
    return None
def verifyLogin():
    tardis.log(l111l1_opy_ (u"ࠧࡆࡰࡷࡩࡷ࡯࡮ࡨ࡙ࠢࡩࡷ࡯ࡦࡺࡎࡲ࡫࡮ࡴࠧࡂ"))
    try:
        global l1l1ll_opy_
        if not l1l1ll_opy_:
            tardis.log(l111l1_opy_ (u"ࠨࡃࡷࡸࡪࡳࡰࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡎࡲ࡫࡮ࡴࠧࡃ"))
            l1llll1l_opy_()
        if not l1l1ll_opy_:
            tardis.log(l111l1_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡒ࡯ࡨ࡫ࡱࠫࡄ"))
            tardis.DialogOK(l111l1_opy_ (u"ࠪࡒࡴࡺࠠ࡭ࡱࡪ࡫ࡪࡪࠠࡪࡰࡷࡳࠥࡌࡩ࡭࡯ࡲࡲ࠳࠭ࡅ"), l111l1_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤࡨ࡮ࡥࡤ࡭ࠣࡨࡪࡺࡡࡪ࡮ࡶࠤࡦࡴࡤࠡࡶࡵࡽࠥࡧࡧࡢ࡫ࡱ࠲ࠬࡆ"))
            return False
        return True
    except Exception, e:
        tardis.log(l111l1_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡛࡫ࡲࡪࡨࡼࡐࡴ࡭ࡩ࡯ࠢࠨࡷࠬࡇ") % str(e))
    return False
def isRecorded(name, start):
    if not verifyLogin():
        return False, None
    l11111l_opy_ = getRecording(name, start)
    if l11111l_opy_ == None:
        tardis.log(l111l1_opy_ (u"࠭ࠥࡴࠢ࡬ࡷࠥࡔࡏࡕࠢࡕࡉࡈࡕࡒࡅࡇࡇࠫࡈ") % name)
        return False, None
    tardis.log(l111l1_opy_ (u"ࠧࠦࡵࠣ࡭ࡸࠦࡒࡆࡅࡒࡖࡉࡋࡄࠨࡉ") % name)
    return True, l11111l_opy_
def record(name, start, end, l1l1l1_opy_, l1llllll_opy_=True):
    output = l111l1_opy_ (u"ࠨࡃࡷࡸࡪࡳࡰࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡵࡨࡸࠥࡸࡥࡤࡱࡵࡨ࡮ࡴࡧࠡࡨࡲࡶࠥࠫࡳࠡࡵࡷࡥࡷࡺ࠺ࠦࡵࠣࡩࡳࡪ࠺ࠦࡵࠣࡷࡹࡸࡥࡢ࡯࠽ࠩࡸ࠭ࡊ") % (name, start, end, l1l1l1_opy_)
    tardis.log(output)
    if not verifyLogin():
        tardis.log(l111l1_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡼࡥࡳ࡫ࡩࡽࠥࡲ࡯ࡨ࡫ࡱࠫࡋ"))
        return False
    global l11l11_opy_
    channel = l1l1l1l_opy_(l1l1l1_opy_)
    if not channel:
        tardis.log(l111l1_opy_ (u"ࠪࡲࡴࡺࠠࡤࡪࡤࡲࡳ࡫࡬ࠨࡌ"))
        tardis.DialogOK(l111l1_opy_ (u"ࠫࡓࡵࠠࡷࡣ࡯࡭ࡩࠦࡣࡩࡣࡱࡲࡪࡲࠠࡧࡱࡸࡲࡩࠦࡩ࡯ࠢࡶࡸࡷ࡫ࡡ࡮࠰ࠪࡍ"), l111l1_opy_ (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥ࡫ࡤࡪࡶࠣࡷࡹࡸࡥࡢ࡯ࠣࡥࡳࡪࠠࡵࡴࡼࠤࡦ࡭ࡡࡪࡰ࠱ࠫࡎ"))
        return False
    l1lll11_opy_ = getProgram(channel, start)
    if not l1lll11_opy_:
        tardis.log(l111l1_opy_ (u"࠭࡮ࡰࡶࠣࡴࡷࡵࡧࡳࡣࡰࠫࡏ"))
        tardis.DialogOK(l111l1_opy_ (u"ࠧࡑࡴࡲ࡫ࡷࡧ࡭ࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡇ࡫࡯ࡱࡴࡴࠠࡨࡷ࡬ࡨࡪ࠴ࠧࡐ"))
        return False
    url     = l11ll1_opy_ % (l11l11_opy_, channel, l1lll11_opy_, l11l_opy_(start))
    record  = l1ll1l1_opy_(url)
    l111ll1_opy_ = False
    tardis.log(l111l1_opy_ (u"ࠨࡴࡨࡧࡴࡸࡤࠡࡶࡤࡷࡰࠦࡵࡳ࡮ࠣ࠾ࠥࠫࡳࠨࡑ") % url)
    tardis.log(l111l1_opy_ (u"ࠩࡵࡩࡸࡶ࡯࡯ࡵࡨࠤࠪࡹࠧࡒ") % record)
    try:
        l1l1lll_opy_ = json.loads(record)
        tardis.log(l111l1_opy_ (u"ࠪࡅࡸࠦࡊࡔࡑࡑࠫࡓ"))
        tardis.log(l1l1lll_opy_)
        if l111l1_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬࡔ") in l1l1lll_opy_:
           l111ll1_opy_ = l1l1lll_opy_[l111l1_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭ࡕ")]
    except Exception, e:
        error = record.split(l111l1_opy_ (u"࠭࠺ࠨࡖ"))[-1].strip()
        tardis.log(l111l1_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡲࡦࡥࡲࡶࡩࠦࠥࡴࠩࡗ") % str(e))
        tardis.log(error)
        if not l1llllll_opy_:
            return False
        tardis.DialogOK(name, l111l1_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡩࡨࡦࡦࡸࡰࡪࠦࡲࡦࡥࡲࡶࡩ࡯࡮ࡨ࠰ࠪࡘ"), error)
        return False
    if not l1llllll_opy_:
        return l1lll11_opy_
    if l111ll1_opy_:
        if end < datetime.datetime.today():
            tardis.DialogOK(name, l111l1_opy_ (u"ࠩࡋࡥࡸࠦࡢࡦࡧࡱࠤࡷ࡫ࡣࡰࡴࡧࡩࡩ࠴࡙ࠧ"))
        else:
            tardis.DialogOK(name, l111l1_opy_ (u"ࠪࡌࡦࡹࠠࡣࡧࡨࡲࠥࡹࡣࡩࡧࡧࡹࡱ࡫ࡤࠡࡶࡲࠤࡧ࡫ࠠࡳࡧࡦࡳࡷࡪࡥࡥ࠰࡚ࠪ"))
    else:
        tardis.DialogOK(l111l1_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡥ࡫ࡩࡩࡻ࡬ࡦࠢࡵࡩࡨࡵࡲࡥ࡫ࡱ࡫࠳࡛࠭"))
    return l1lll11_opy_
def getRecording(name, start):
    if not verifyLogin():
        return False
    global l11l11_opy_
    url        = l11l111_opy_ % l11l11_opy_
    l1l11ll_opy_ = l1ll1l1_opy_(url)
    l1l11ll_opy_ = json.loads(l1l11ll_opy_)
    l1l11ll_opy_ = l1l11ll_opy_[l111l1_opy_ (u"ࠬࡸࡥࡤࡱࡵࡨ࡮ࡴࡧࡴࠩ࡜")]
    l1lll_opy_ = l11l_opy_(start)
    name    = name.lower()
    for l11111l_opy_ in l1l11ll_opy_:
        try:
            title = l11111l_opy_[l111l1_opy_ (u"࠭ࡴࡪࡶ࡯ࡩࠬ࡝")].lower()
            start = int(l11111l_opy_[l111l1_opy_ (u"ࠧࡵ࡫ࡰࡩࡤࡹࡴࡢࡴࡷࠫ࡞")])
            if (start == l1lll_opy_):
                tardis.log(l111l1_opy_ (u"ࠨࡆࡲࡻࡳࡲ࡯ࡢࡦ࡙ࠣࡗࡒࠠ࠾ࠢࠨࡷࠬ࡟") % l11111l_opy_[l111l1_opy_ (u"ࠩࡧࡳࡼࡴ࡬ࡰࡣࡧࡣࡺࡸ࡬ࠨࡠ")])
                return l11111l_opy_[l111l1_opy_ (u"ࠪࡨࡴࡽ࡮࡭ࡱࡤࡨࡤࡻࡲ࡭ࠩࡡ")]
        except Exception, e:
            tardis.log(l111l1_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡵࡪࡵࡳࡼࡴࠠࡪࡰࠣ࡫ࡪࡺࡒࡦࡥࡲࡶࡩ࡯࡮ࡨࠢࠨࡷࠬࡢ") % str(e))
    return None
def getHDTVRecording(name, title, start, stream):
    tardis.log(l111l1_opy_ (u"ࠬࡥ࡟ࡠࡡࡢࡣࡤࡥ࡟ࠡࡅࡄࡘࡈࡎࠠࡖࡒࠣࡌࡉ࡚ࡖࠡࡡࡢࡣࡤࡥ࡟ࡠࡡࡢࡣࠬࡣ"))
    tardis.log(name)
    tardis.log(title)
    tardis.log(start)
    tardis.log(stream)
    import urllib
    l11llll_opy_ = l1lll1_opy_()
    tardis.log(l111l1_opy_ (u"࠭ࡅࡑࡉࠣࡗࡹࡧࡲࡵࠢࡗ࡭ࡲ࡫࠮࠯࠰࠽ࠤࠪࡹࠧࡤ") % start)
    tardis.log(l111l1_opy_ (u"ࠧࡐࡨࡩࡷࡪࡺࠠࡪࡰࠣࡷࡪࡩ࡯࡯ࡦࡶ࠾ࠥࠫࡳࠨࡥ") % l11llll_opy_)
    l1lllll1_opy_  =  start - datetime.timedelta(seconds=l11llll_opy_)
    tardis.log(l111l1_opy_ (u"ࠨࡕࡷࡥࡷࡺࠠࡕ࡫ࡰࡩࠥࡵࡦࡧࡵࡨࡸ࠿ࠦࠥࡴࠩࡦ") % l1lllll1_opy_)
    l1111_opy_ =  str(l1lllll1_opy_)
    l1l1_opy_  =  l1111_opy_.split(l111l1_opy_ (u"ࠩࠣࠫࡧ"))[0]
    l1ll1ll_opy_  =  getRecordURL(name)
    if l1ll1ll_opy_ is None:
        tardis.DialogOK(l111l1_opy_ (u"ࠪࡗࡴࡸࡲࡺ࠰ࠪࡨ"), l111l1_opy_ (u"ࠫ࡜࡫ࠠࡤࡱࡸࡰࡩࠦ࡮ࡰࡶࠣࡪ࡮ࡴࡤࠡࡣࠣࡧࡦࡺࡣࡩࡷࡳࠤࡸ࡫ࡲࡷ࡫ࡦࡩࠥ࡬࡯ࡳࠢࡷ࡬࡮ࡹࠠࡤࡪࡤࡲࡳ࡫࡬࠯ࠩࡩ"), l111l1_opy_ (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥࡺࡲࡺࠢࡤࡲࡴࡺࡨࡦࡴࠣࡧ࡭ࡧ࡮࡯ࡧ࡯࠲ࠬࡪ"))
        return None
    l1l1111_opy_  =  l1111_opy_.split(l111l1_opy_ (u"࠭࠭ࠨ࡫"), 1)[-1].rsplit(l111l1_opy_ (u"ࠧ࠻ࠩ࡬"), 1)[0]
    l11l1_opy_    =  urllib.quote_plus(l1l1111_opy_)
    l111l1l_opy_  = l111l1_opy_ (u"ࠨࡲ࡯ࡳࡹࡃࠧ࡭") + l11l1_opy_
    l1111l_opy_    =  l1ll1l_opy_(stream)
    tardis.log(l1111l_opy_)
    l1ll_opy_ = l111l1_opy_ (u"ࠩࡾࠦ࡯ࡹ࡯࡯ࡴࡳࡧࠧࡀࠢ࠳࠰࠳ࠦ࠱ࠦࠢ࡮ࡧࡷ࡬ࡴࡪࠢ࠻ࠤࡉ࡭ࡱ࡫ࡳ࠯ࡉࡨࡸࡉ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠭ࠢࠥࡴࡦࡸࡡ࡮ࡵࠥ࠾ࢀࠨࡤࡪࡴࡨࡧࡹࡵࡲࡺࠤ࠽ࠦࡵࡲࡵࡨ࡫ࡱ࠾࠴࠵ࠥࡴࠤࢀ࠰ࠥࠨࡩࡥࠤ࠽ࠤ࠶ࢃࠧ࡮") % l1111l_opy_
    l111lll_opy_ = l111l1_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠽࠳࠴ࠫࡳ࠰ࡁࡤࡧࡹ࡯࡯࡯࠿࡯࡭ࡻ࡫ࡴࡷࡡࡦࡥࡹࡩࡨࡶࡲࡢࡦࡾࡥࡣࡩࡣࡱࡲࡪࡲ࡟ࡢࡰࡧࡣࡩࡧࡴࡦࠨࡨࡼࡹࡸࡡࠧࡲࡤ࡫ࡪࠬࡰ࡭ࡱࡷࠪࡹ࡮ࡵ࡮ࡤࡱࡥ࡮ࡲࠦࡵ࡫ࡷࡰࡪࡃࠥࡴࠨࡸࡶࡱࡃࠥࡴࠩ࡯") % (l1111l_opy_, l1l1_opy_, l1ll1ll_opy_)
    l11l1ll_opy_ = l111l1_opy_ (u"ࠫࢀࠨࡪࡴࡱࡱࡶࡵࡩࠢ࠻ࠤ࠵࠲࠵ࠨࠬࠡࠤࡰࡩࡹ࡮࡯ࡥࠤ࠽ࠦࡋ࡯࡬ࡦࡵ࠱ࡋࡪࡺࡄࡪࡴࡨࡧࡹࡵࡲࡺࠤ࠯ࠤࠧࡶࡡࡳࡣࡰࡷࠧࡀࡻࠣࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠦ࠿ࠨࠥࡴࠤࢀ࠰ࠥࠨࡩࡥࠤ࠽ࠤ࠶ࢃࠧࡰ") % l111lll_opy_
    l1ll111_opy_    =  xbmc.executeJSONRPC(l11l1ll_opy_)
    response   =  json.loads(l1ll111_opy_)
    result     =  response[l111l1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬࡱ")]
    l1l11ll_opy_ =  result[l111l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡷࠬࡲ")]
    for l11111l_opy_ in l1l11ll_opy_:
        try:
            l1lll11_opy_ = l11111l_opy_[l111l1_opy_ (u"ࠧࡧ࡫࡯ࡩࠬࡳ")]
            if l111l1l_opy_ in l1lll11_opy_:
                tardis.DialogOK(l111l1_opy_ (u"ࠨ࡝ࡆࡓࡑࡕࡒࠡࡱࡵࡥࡳ࡭ࡥ࡞ࡅࡤࡸࡨ࡮࠭ࡶࡲࠣࡷࡹࡸࡥࡢ࡯ࠣࡪࡴࡻ࡮ࡥ࠰࡞࠳ࡈࡕࡌࡐࡔࡠࠫࡴ"), l111l1_opy_ (u"ࠩࡒࡲ࠲࡚ࡡࡱࡲ࠱ࡘ࡛ࠦࡷࡪ࡮࡯ࠤࡳࡵࡷࠡࡲ࡯ࡥࡾࡀࠠ࡜ࡅࡒࡐࡔࡘࠠࡰࡴࡤࡲ࡬࡫࡝࡜ࡄࡠࠩࡸࡡ࠯ࡃ࡟࡞࠳ࡈࡕࡌࡐࡔࡠࠫࡵ") % (title))
                tardis.log(l111l1_opy_ (u"ࠪࡴࡷࡵࡧࡳࡣࡰࡍࡉ࠭ࡶ"))
                tardis.log(l111l1l_opy_)
                return l1lll11_opy_
        except Exception, e:
            tardis.log(l111l1_opy_ (u"ࠫࡊࡘࡒࡐࡔ࠽ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡵࡪࡵࡳࡼࡴࠠࡪࡰࠣ࡫ࡪࡺࡈࡅࡖ࡙ࡖࡪࡩ࡯ࡳࡦ࡬ࡲ࡬ࠦࠥࡴࠩࡷ") % str(e))
            tardis.DialogOK(l111l1_opy_ (u"࡙ࠬ࡯ࡳࡴࡼ࠲ࠬࡸ"), l111l1_opy_ (u"࠭ࡗࡦࠢࡦࡳࡺࡲࡤࠡࡰࡲࡸࠥ࡬ࡩ࡯ࡦࠣࡥࠥࡩࡡࡵࡥ࡫ࡹࡵࠦࡳࡵࡴࡨࡥࡲࠦࡦࡰࡴࠣࡸ࡭࡯ࡳࠡࡲࡵࡳ࡬ࡸࡡ࡮࠰ࠪࡹ"), l111l1_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡵࡴࡼࠤࡦ࡭ࡡࡪࡰࠣࡰࡦࡺࡥࡳ࠰ࠪࡺ"))
            return None
def l1ll1l_opy_(stream):
    if stream.startswith(l111l1_opy_ (u"ࠨࡊࡇࡘ࡛ࡀࠧࡻ")):
        return l111l1_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡪࡧࡸࡻ࠭ࡼ")
    if stream.startswith(l111l1_opy_ (u"ࠪࡌࡉ࡚ࡖ࠳࠼ࠪࡽ")):
        return l111l1_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡶࡺࡿࡡࡪࡲࡷࡺࠬࡾ")
    if stream.startswith(l111l1_opy_ (u"ࠬࡎࡄࡕࡘ࠶࠾ࠬࡿ")):
        return l111l1_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡸࡵࡺࡣࡷࡺࠬࢀ")
    if stream.startswith(l111l1_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠺࠰࠱ࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡺ࡯ࠫࢁ")):
        return l111l1_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡹ࡮ࠪࢂ")
def getRecordURL(name):
    l11lll_opy_   = tardis.PROFILE
    l1l_opy_ = os.path.join(l11lll_opy_, l111l1_opy_ (u"ࠩ࡬ࡲ࡮࠭ࢃ"), l111l1_opy_ (u"ࠪࡧࡦࡺࡣࡩࡷࡳ࠲ࡹࡾࡴࠨࢄ"))
    l1lll11l_opy_   = json.load(open(l1l_opy_))
    for channel in l1lll11l_opy_:
        if name.upper() == channel[l111l1_opy_ (u"ࠫࡔ࡚ࡔࡗࠩࢅ")].upper():
            return channel[l111l1_opy_ (u"࡛ࠬࡒࡍࠩࢆ")]
def l1lll1_opy_():
    tardis.log(l111l1_opy_ (u"࠭࡟ࡠࡡࡢࡣࡤࠦࡇࡦࡶࠣࡘ࡮ࡳࡥࠡࡑࡩࡪࡸ࡫ࡴࠡࡡࡢࡣࡤࡥ࡟ࠨࢇ"))
    import time
    gmt = time.gmtime()
    loc = time.localtime()
    GMT = datetime.datetime(*gmt[:6]).isoformat(l111l1_opy_ (u"ࠧࠡࠩ࢈"))
    LOC = datetime.datetime(*loc[:6]).isoformat(l111l1_opy_ (u"ࠨࠢࠪࢉ"))
    tardis.log(gmt)
    tardis.log(loc)
    l1_opy_ = tardis.parseTime(GMT)
    l111l_opy_ = tardis.parseTime(LOC)
    tardis.log(l1_opy_)
    tardis.log(l111l_opy_)
    tardis.log(l111l1_opy_ (u"ࠩࡢࡣࡤࡥ࡟ࡠࡡࡢࡣࡤࠦࡏࡇࡈࡖࡉ࡙ࠦ࡟ࡠࡡࡢࡣࡤࡥ࡟ࡠࡡࡢࠫࢊ"))
    l11llll_opy_ = l1_opy_ - l111l_opy_
    tardis.log(l11llll_opy_)
    l11llll_opy_ = ((l11llll_opy_.days * 86400) + (l11llll_opy_.seconds + 1800)) / 3600
    tardis.log(l11llll_opy_)
    l11llll_opy_ *= -3600
    tardis.log(l11llll_opy_)
    tardis.log(l111l1_opy_ (u"ࠪࡣࡤࡥ࡟ࡠࡡࡢࡣࡤࡥ࡟ࡠࡡࡢࡣࡤࡥ࡟ࡠࡡࡢࡣࡤࡥ࡟ࡠࡡࡢࡣࠬࢋ"))
    return l11llll_opy_
def l1111ll_opy_(url):
    if not verifyLogin():
        return False
    try:
        l111l1l_opy_ = url.rsplit(l111l1_opy_ (u"ࠫ࠴࠭ࢌ"), 1)[-1].split(l111l1_opy_ (u"ࠬ࠴ࠧࢍ"), 1)[0]
        global l11l11_opy_
        url        = l1l1l11_opy_ % (l11l11_opy_, l111l1l_opy_)
        response   = l1ll1l1_opy_(url)
        response   = json.loads(response)
    except:
        pass