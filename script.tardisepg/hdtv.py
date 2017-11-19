# coding: UTF-8
import sys
l1llll11_opy_ = sys.version_info [0] == 2
l1ll11l_opy_ = 2048
l1ll1l_opy_ = 7
def l1111l_opy_ (ll_opy_):
	global l111_opy_
	l1111l1_opy_ = ord (ll_opy_ [-1])
	l1lllll1_opy_ = ll_opy_ [:-1]
	l1ll1_opy_ = l1111l1_opy_ % len (l1lllll1_opy_)
	l11l11l_opy_ = l1lllll1_opy_ [:l1ll1_opy_] + l1lllll1_opy_ [l1ll1_opy_:]
	if l1llll11_opy_:
		l1l1ll1_opy_ = unicode () .join ([unichr (ord (char) - l1ll11l_opy_ - (l11l1l_opy_ + l1111l1_opy_) % l1ll1l_opy_) for l11l1l_opy_, char in enumerate (l11l11l_opy_)])
	else:
		l1l1ll1_opy_ = str () .join ([chr (ord (char) - l1ll11l_opy_ - (l11l1l_opy_ + l1111l1_opy_) % l1ll1l_opy_) for l11l1l_opy_, char in enumerate (l11l11l_opy_)])
	return eval (l1l1ll1_opy_)
import xbmc
import xbmcgui
import time
import datetime
import os
import sys
from threading import Timer
if sys.version_info >=  (2, 7):
    import json
else:
    import simplejson as json
import tardis
PATH     =  os.path.join(tardis.PROFILE, l1111l_opy_ (u"࠭ࡴࡦ࡯ࡳࠫࢎ"))
SETTING  = l1111l_opy_ (u"ࠧࡍࡑࡊࡍࡓࡥࡈࡅࡖ࡙ࠫ࢏")
l1l11l_opy_ =  50
def getURL(url):
    if tardis.validTime(SETTING, 60 * 60 * 8):
        response = json.load(open(PATH))
    else:
        response = l1l1l1l1_opy_(url)
        l1lll1_opy_(SETTING)
    stream = url.split(l1111l_opy_ (u"ࠨ࠼ࠪ࢐"), 1)[-1].lower()
    try:
        result = response[l1111l_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩ࢑")]
        l1lll111_opy_  = result[l1111l_opy_ (u"ࠪࡪ࡮ࡲࡥࡴࠩ࢒")]
    except Exception as e:
        l1l11ll1_opy_(e)
        return None
    for file in l1lll111_opy_:
        l1l1lll1_opy_   = file[l1111l_opy_ (u"ࠫࡱࡧࡢࡦ࡮ࠪ࢓")]
        l1l1lll1_opy_   = l1l1lll1_opy_.replace(l1111l_opy_ (u"ࠬࠦࠠࠨ࢔"), l1111l_opy_ (u"࠭ࠠࠨ࢕")).replace(l1111l_opy_ (u"ࠧࠡ࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪ࢖"), l1111l_opy_ (u"ࠨ࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪࢗ"))
        channel = l1l1lll1_opy_.rsplit(l1111l_opy_ (u"ࠩ࡞࠳ࡈࡕࡌࡐࡔࡠࠫ࢘"), 1)[0].split(l1111l_opy_ (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡻ࡭࡯ࡴࡦ࡟࢙ࠪ"), 1)[-1]
        if stream == channel.lower():
            return file[l1111l_opy_ (u"ࠫ࡫࡯࡬ࡦ࢚ࠩ")]
    return None
def l1l1l1l1_opy_(url):
    try:
        message = l1111l_opy_ (u"ࠬࡘࡥࡵࡴ࡬ࡩࡻ࡯࡮ࡨࠢࡸࡴࡩࡧࡴࡦࡦࠣࡧ࡭ࡧ࡮࡯ࡧ࡯ࠤࡱ࡯࡮࡬ࡵ࠱ࠤࡕࡲࡥࡢࡵࡨࠤࡧ࡫ࠠࡱࡣࡷ࡭ࡪࡴࡴ࠯࢛ࠩ")
        tardis.notify(message, 7000)
        tardis.ShowBusy()
        response = l1ll11ll_opy_(url)
        tardis.CloseBusy()
        return response
    except Exception as e:
        l1l11ll1_opy_(e)
        return {l1111l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠬ࢜") : l1111l_opy_ (u"ࠧࡑ࡮ࡸ࡫࡮ࡴࠠࡆࡴࡵࡳࡷ࠭࢝")}
def l1ll11ll_opy_(url):
    doJSON(url)
    return json.load(open(PATH))
def doJSON(url):
    l11ll11_opy_ = l1ll1lll_opy_(url)
    xbmc.executeJSONRPC(l11ll11_opy_)
    l1ll1ll1_opy_  = l1ll1111_opy_(url)
    response = xbmc.executeJSONRPC(l1ll1ll1_opy_)
    content = json.loads(response.decode(l1111l_opy_ (u"ࠨ࡮ࡤࡸ࡮ࡴ࠭࠲ࠩ࢞"), l1111l_opy_ (u"ࠩ࡬࡫ࡳࡵࡲࡦࠩ࢟")))
    json.dump(content, open(PATH,l1111l_opy_ (u"ࠪࡻࠬࢠ")), indent=0)
    l1ll11l1_opy_(url)
def l1ll1lll_opy_(url):
    l11111_opy_ = l1llll_opy_(url)
    l11ll11_opy_   = (l1111l_opy_ (u"ࠫࢀࠨࡪࡴࡱࡱࡶࡵࡩࠢ࠻ࠤ࠵࠲࠵ࠨࠬࠡࠤࡰࡩࡹ࡮࡯ࡥࠤ࠽ࠦࡋ࡯࡬ࡦࡵ࠱ࡋࡪࡺࡄࡪࡴࡨࡧࡹࡵࡲࡺࠤ࠯ࠤࠧࡶࡡࡳࡣࡰࡷࠧࡀࡻࠣࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠦ࠿ࠨࡰ࡭ࡷࡪ࡭ࡳࡀ࠯࠰ࠧࡶ࠳ࡄࡧࡣࡵ࡫ࡲࡲࡂࡳࡡࡪࡰࡢࡰ࡮ࡹࡴࠧࡶ࡬ࡸࡱ࡫࠽ࠧࡷࡵࡰࡂࠨࡽ࠭ࠢࠥ࡭ࡩࠨ࠺ࠡ࠳ࢀࠫࢡ") % l11111_opy_)
    return l11ll11_opy_
def l1ll1111_opy_(url):
    l11111_opy_ = l1llll_opy_(url)
    l1ll1ll1_opy_ = (l1111l_opy_ (u"ࠬࢁࠢ࡫ࡵࡲࡲࡷࡶࡣࠣ࠼ࠥ࠶࠳࠶ࠢ࠭ࠢࠥࡱࡪࡺࡨࡰࡦࠥ࠾ࠧࡌࡩ࡭ࡧࡶ࠲ࡌ࡫ࡴࡅ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠥ࠰ࠥࠨࡰࡢࡴࡤࡱࡸࠨ࠺ࡼࠤࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧࡀࠢࡱ࡮ࡸ࡫࡮ࡴ࠺࠰࠱ࠨࡷ࠴ࡅࡡࡤࡶ࡬ࡳࡳࡃ࡬ࡪࡸࡨࡸࡻࡥࡡ࡭࡮ࠩࡸ࡮ࡺ࡬ࡦ࠿ࡄࡰࡱ࠱ࡣࡩࡣࡱࡲࡪࡲࡳࠣࡿ࠯ࠤࠧ࡯ࡤࠣ࠼ࠣ࠵ࢂ࠭ࢢ") % l11111_opy_)
    return l1ll1ll1_opy_
def l1llll_opy_(url):
    if url.startswith(l1111l_opy_ (u"࠭ࡈࡅࡖ࡙࠾ࠬࢣ")):
        return l1111l_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡨࡥࡶࡹࠫࢤ")
    if url.startswith(l1111l_opy_ (u"ࠨࡊࡇࡘ࡛࠸࠺ࠨࢥ")):
        return l1111l_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡴࡸࡽࡦ࡯ࡰࡵࡸࠪࢦ")
    if url.startswith(l1111l_opy_ (u"ࠪࡌࡉ࡚ࡖ࠴࠼ࠪࢧ")):
        return l1111l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡶࡺࡿࡡࡵࡸࠪࢨ")
def l1l11lll_opy_(url):
    HOME = tardis.PROFILE
    l1l1l11l_opy_ = l1111l_opy_ (u"ࠬ࡮ࡤࡵࡸࡰࡥࡸࡺࡥࡳ࠰࡬ࡲ࡮࠭ࢩ")
    l1l11l1l_opy_  = os.path.join(HOME, l1l1l11l_opy_)
    l11l1l1_opy_ = l1llll_opy_(url)
    response = json.load(open(PATH))
    result   = response[l1111l_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ࢪ")]
    l1lll11l_opy_ = result[l1111l_opy_ (u"ࠧࡧ࡫࡯ࡩࡸ࠭ࢫ")]
    l1l1ll1l_opy_  = file(l1l11l1l_opy_, l1111l_opy_ (u"ࠨࡹࠪࢬ"))
    l1l1ll1l_opy_.write(l1111l_opy_ (u"ࠩ࡞ࠫࢭ"))
    l1l1ll1l_opy_.write(l11l1l1_opy_)
    l1l1ll1l_opy_.write(l1111l_opy_ (u"ࠪࡡࠬࢮ"))
    l1l1ll1l_opy_.write(l1111l_opy_ (u"ࠫࡡࡴࠧࢯ"))
    for channel in l1lll11l_opy_:
        l1l1lll1_opy_    = channel[l1111l_opy_ (u"ࠬࡲࡡࡣࡧ࡯ࠫࢰ")].replace(l1111l_opy_ (u"࠭ࠠࠡࠩࢱ"), l1111l_opy_ (u"ࠧࠡࠩࢲ")).replace(l1111l_opy_ (u"ࠨࠢ࡞࠳ࡈࡕࡌࡐࡔࡠࠫࢳ"), l1111l_opy_ (u"ࠩ࡞࠳ࡈࡕࡌࡐࡔࡠࠫࢴ"))
        l1l1l111_opy_  = l1l1lll1_opy_.rsplit(l1111l_opy_ (u"ࠪ࡟࠴ࡉࡏࡍࡑࡕࡡࠬࢵ"), 1)[0].split(l1111l_opy_ (u"ࠫࡠࡉࡏࡍࡑࡕࠤࡼ࡮ࡩࡵࡧࡠࠫࢶ"), 1)[-1]
        l1ll1l11_opy_ = channel[l1111l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࠪࢷ")]
        if l1111l_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳࡮ࡤࡵࡸࠪࢸ") in channel[l1111l_opy_ (u"ࠧࡧ࡫࡯ࡩࠬࢹ")]:
            l1ll1l11_opy_ = l1111l_opy_ (u"ࠨࡊࡇࡘ࡛ࡀࠧࢺ") + l1l1l111_opy_
        if l1111l_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡴࡸࡽࡦ࡯ࡰࡵࡸࠪࢻ") in channel[l1111l_opy_ (u"ࠪࡪ࡮ࡲࡥࠨࢼ")]:
            l1ll1l11_opy_ = l1111l_opy_ (u"ࠫࡍࡊࡔࡗ࠴࠽ࠫࢽ") + l1l1l111_opy_
        if l1111l_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡷࡻࡹࡢࡶࡹࠫࢾ") in channel[l1111l_opy_ (u"࠭ࡦࡪ࡮ࡨࠫࢿ")]:
            l1ll1l11_opy_ = l1111l_opy_ (u"ࠧࡉࡆࡗ࡚࠷ࡀࠧࣀ") + l1l1l111_opy_
        l1l1ll1l_opy_.write(l1111l_opy_ (u"ࠨࠧࡶࠫࣁ") % l1l1l111_opy_)
        l1l1ll1l_opy_.write(l1111l_opy_ (u"ࠩࡀࠫࣂ"))
        l1l1ll1l_opy_.write(l1111l_opy_ (u"ࠪࠩࡸ࠭ࣃ") % l1ll1l11_opy_)
        l1l1ll1l_opy_.write(l1111l_opy_ (u"ࠫࡡࡴࠧࣄ"))
    l1l1ll1l_opy_.write(l1111l_opy_ (u"ࠬࡢ࡮ࠨࣅ"))
    l1l1ll1l_opy_.close()
def l1ll11l1_opy_(url):
    name   = tardis.TITLE + l1111l_opy_ (u"࠭ࠠࡉࡆࡗ࡚࡛ࠥࡰࡥࡣࡷࡩࠬࣆ")
    l1ll1l1l_opy_ = os.path.join(tardis.HOME, l1111l_opy_ (u"ࠧࡩࡦࡷࡺ࠳ࡶࡹࠨࣇ"))
    args   = url
    cmd    = l1111l_opy_ (u"ࠨࡃ࡯ࡥࡷࡳࡃ࡭ࡱࡦ࡯࠭ࠫࡳ࠭ࠢࡕࡹࡳ࡙ࡣࡳ࡫ࡳࡸ࠭ࠫࡳ࠭ࠢࠨࡷ࠮࠲ࠠࠦࡦ࠯ࠤ࡙ࡸࡵࡦࠫࠪࣈ") % (name, l1ll1l1l_opy_, args, l1l11l_opy_)
    xbmc.executebuiltin(l1111l_opy_ (u"ࠩࡆࡥࡳࡩࡥ࡭ࡃ࡯ࡥࡷࡳࠨࠦࡵ࠯ࡘࡷࡻࡥࠪࠩࣉ") % name)
    xbmc.executebuiltin(cmd)
def l1lll1_opy_(l1l1ll11_opy_):
    now = datetime.datetime.today()
    tardis.SetSetting(l1l1ll11_opy_, str(now))
def l1l11ll1_opy_(e):
    l1l1llll_opy_ = l1111l_opy_ (u"ࠪࡗࡴࡸࡲࡺ࠮ࠣࡥࡳࠦࡥࡳࡴࡲࡶࠥࡵࡣࡤࡷࡵࡩࡩࡀࠠࡋࡕࡒࡒࠥࡋࡲࡳࡱࡵ࠾ࠥࠫࡳࠨ࣊")  %e
    l1l1l1ll_opy_ = l1111l_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤࡷ࡫࠭࡭࡫ࡱ࡯ࠥࡺࡨࡪࡵࠣࡧ࡭ࡧ࡮࡯ࡧ࡯ࠤࡦࡴࡤࠡࡶࡵࡽࠥࡧࡧࡢ࡫ࡱ࠲ࠬ࣋")
    l1ll111l_opy_ = l1111l_opy_ (u"࡛ࠬࡳࡦ࠼ࠣࡇࡴࡴࡴࡦࡺࡷࠤࡒ࡫࡮ࡶࠢࡀࡂࠥࡘࡥ࡮ࡱࡹࡩ࡙ࠥࡴࡳࡧࡤࡱࠬ࣌")
    tardis.log(e)
    tardis.DialogOK(l1l1llll_opy_, l1l1l1ll_opy_, l1ll111l_opy_)
    tardis.SetSetting(SETTING, l1111l_opy_ (u"࠭ࠧ࣍"))
if __name__ == l1111l_opy_ (u"ࠧࡠࡡࡰࡥ࡮ࡴ࡟ࡠࠩ࣎"):
    url = sys.argv[1]
    doJSON(url)