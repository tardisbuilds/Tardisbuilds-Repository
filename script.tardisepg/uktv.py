# coding: UTF-8
import sys
l11ll111_opy_ = sys.version_info [0] == 2
l1lll1l1_opy_ = 2048
l11lllll_opy_ = 7
def l1l11_opy_ (l11ll1_opy_):
	global l1llll11_opy_
	l1ll1111_opy_ = ord (l11ll1_opy_ [-1])
	l11ll11l_opy_ = l11ll1_opy_ [:-1]
	l11l11l_opy_ = l1ll1111_opy_ % len (l11ll11l_opy_)
	l111l1_opy_ = l11ll11l_opy_ [:l11l11l_opy_] + l11ll11l_opy_ [l11l11l_opy_:]
	if l11ll111_opy_:
		l1lll1_opy_ = unicode () .join ([unichr (ord (char) - l1lll1l1_opy_ - (l1l1l_opy_ + l1ll1111_opy_) % l11lllll_opy_) for l1l1l_opy_, char in enumerate (l111l1_opy_)])
	else:
		l1lll1_opy_ = str () .join ([chr (ord (char) - l1lll1l1_opy_ - (l1l1l_opy_ + l1ll1111_opy_) % l11lllll_opy_) for l1l1l_opy_, char in enumerate (l111l1_opy_)])
	return eval (l1lll1_opy_)
import xbmc
import xbmcaddon
import json
import urllib
import os
import tardis
l1llll1ll_opy_   = l1l11_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡶ࡭ࡷࡺ࡫ࡸࡡ࡯ࡥࡨࠫ࡟")
l1lll1111_opy_   = l1l11_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡺࡷࡶࡪࡧ࡭࠮ࡥࡲࡨࡪࡹࠧࡠ")
l1llll111_opy_ = l1l11_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰࡬ࡴࡹࡼࡳࡶࡤࡶࠫࡡ")
l1ll1lll1_opy_   = l1l11_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡨࡪࡾࠧࡢ")
l1ll11l11_opy_    = l1l11_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡶࡻࡩࡤ࡭࡬ࡴࡹࡼࠧࡣ")
l1ll11ll1_opy_   = l1l11_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳࡬ࡵࡵࡷࡵࡩࡸࡺࡲࡦࡣࡰࡷࠬࡤ")
l1llll1l1_opy_  = l1l11_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡳࡵࡧࡤࡰࡹ࡮ࡵ࡯ࡦࡨࡶ࡬ࡸ࡯ࡶࡰࡧࠫࡥ")
l1ll1111l_opy_   =  [l1llll1ll_opy_, l1lll1111_opy_, l1llll111_opy_, l1ll1lll1_opy_, l1ll11l11_opy_, l1ll11ll1_opy_, l1llll1l1_opy_]
def checkAddons():
    for l1ll1l11l_opy_ in l1ll1111l_opy_:
        if l1lll11ll_opy_(l1ll1l11l_opy_):
            l1lll1l11_opy_(l1ll1l11l_opy_)
def l1lll11ll_opy_(l1ll1l11l_opy_):
    if xbmc.getCondVisibility(l1l11_opy_ (u"ࠨࡕࡼࡷࡹ࡫࡭࠯ࡊࡤࡷࡆࡪࡤࡰࡰࠫࠩࡸ࠯ࠧࡦ") % l1ll1l11l_opy_) == 1:
        return True
    else:
        return False
def l1lll1l11_opy_(l1ll1l11l_opy_):
    HOME = tardis.PROFILE
    PATH = os.path.join(HOME, l1l11_opy_ (u"ࠩ࡬ࡲ࡮࠭ࡧ"))
    l11111l1_opy_ = l1lll1lll_opy_(l1ll1l11l_opy_) + l1l11_opy_ (u"ࠪ࠲࡮ࡴࡩࠨࡨ")
    l1ll11l1l_opy_  = os.path.join(PATH, l11111l1_opy_)
    response = l111l111_opy_(l1ll1l11l_opy_)
    try:
        result = response[l1l11_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫࡩ")]
    except KeyError:
        tardis.log(l1l11_opy_ (u"ࠬ࠳࠭࠮࠯࠰ࠤࡐ࡫ࡹࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡪࡩࡹࡌࡩ࡭ࡧࡶࠤ࠲࠳࠭࠮࠯ࠣࠫࡪ") + l1ll1l11l_opy_)
        result = {l1l11_opy_ (u"ࡻࠧࡧ࡫࡯ࡩࡸ࠭࡫"): [{l1l11_opy_ (u"ࡵࠨࡨ࡬ࡰࡪࡺࡹࡱࡧࠪ࡬"): l1l11_opy_ (u"ࡶࠩࡩ࡭ࡱ࡫ࠧ࡭"), l1l11_opy_ (u"ࡷࠪࡸࡾࡶࡥࠨ࡮"): l1l11_opy_ (u"ࡸࠫࡺࡴ࡫࡯ࡱࡺࡲࠬ࡯"), l1l11_opy_ (u"ࡹࠬ࡬ࡩ࡭ࡧࠪࡰ"): l1l11_opy_ (u"ࡺ࠭ࡰ࡭ࡷࡪ࡭ࡳࡀ࠯࠰ࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡹࡺࡻࠫࡱ"), l1l11_opy_ (u"ࡻࠧ࡭ࡣࡥࡩࡱ࠭ࡲ"): l1l11_opy_ (u"ࡵࠨࡐࡒࠤࡈࡎࡁࡏࡐࡈࡐࡘ࠭ࡳ")}], l1l11_opy_ (u"ࡶࠩ࡯࡭ࡲ࡯ࡴࡴࠩࡴ"): {l1l11_opy_ (u"ࡷࠪࡷࡹࡧࡲࡵࠩࡵ"): 0, l1l11_opy_ (u"ࡸࠫࡹࡵࡴࡢ࡮ࠪࡶ"): 1, l1l11_opy_ (u"ࡹࠬ࡫࡮ࡥࠩࡷ"): 1}}
    l1ll1l111_opy_ = result[l1l11_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡶࠫࡸ")]
    l1111l11_opy_  = file(l1ll11l1l_opy_, l1l11_opy_ (u"࠭ࡷࠨࡹ"))
    l1111l11_opy_.write(l1l11_opy_ (u"ࠧ࡜ࠩࡺ"))
    l1111l11_opy_.write(l1ll1l11l_opy_)
    l1111l11_opy_.write(l1l11_opy_ (u"ࠨ࡟ࠪࡻ"))
    l1111l11_opy_.write(l1l11_opy_ (u"ࠩ࡟ࡲࠬࡼ"))
    l1lll111l_opy_ = []
    for channel in l1ll1l111_opy_:
        l1lll1ll1_opy_ = channel[l1l11_opy_ (u"ࠪࡰࡦࡨࡥ࡭ࠩࡽ")]
        if l1l11_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡨࡪࡾࠧࡾ") in channel[l1l11_opy_ (u"ࠬ࡬ࡩ࡭ࡧࠪࡿ")]:
            stream = channel[l1l11_opy_ (u"࠭ࡦࡪ࡮ࡨࠫࢀ")].replace(l1l11_opy_ (u"ࠧ࠯ࡶࡶࠫࢁ"), l1l11_opy_ (u"ࠨ࠰ࡰ࠷ࡺ࠾ࠧࢂ"))
        else:
            stream  = channel[l1l11_opy_ (u"ࠩࡩ࡭ࡱ࡫ࠧࢃ")]
        l1lll1l1l_opy_  = l1ll1ll11_opy_(l1ll1l11l_opy_, l1lll1ll1_opy_)
        channel = l1ll1ll1l_opy_(l1ll1l11l_opy_, l1lll1l1l_opy_)
        l111111l_opy_ = channel + l1l11_opy_ (u"ࠪࡁࠬࢄ") + stream
        l1lll111l_opy_.append(l111111l_opy_)
        l1lll111l_opy_.sort()
    for item in l1lll111l_opy_:
      l1111l11_opy_.write(l1l11_opy_ (u"ࠦࠪࡹ࡜࡯ࠤࢅ") % item)
    l1111l11_opy_.close()
def l1lll1lll_opy_(l1ll1l11l_opy_):
    if l1ll1l11l_opy_ == l1llll1ll_opy_:
        return l1l11_opy_ (u"ࠬࡻ࡫ࡵࡸࡩࡶࡦࡴࡣࡦࠩࢆ")
    if l1ll1l11l_opy_ == l1lll1111_opy_:
        return l1l11_opy_ (u"࠭ࡸࡵࡴࡨࡥࡲ࠳ࡣࡰࡦࡨࡷࠬࢇ")
    if l1ll1l11l_opy_ == l1llll111_opy_:
        return l1l11_opy_ (u"ࠧࡪࡲࡷࡺࡸࡻࡢࡴࠩ࢈")
    if l1ll1l11l_opy_ == l1ll1lll1_opy_:
        return l1l11_opy_ (u"ࠨࡦࡨࡼࠬࢉ")
    if l1ll1l11l_opy_ == l1ll11l11_opy_:
        return l1l11_opy_ (u"ࠩࡴࡹ࡮ࡩ࡫ࠨࢊ")
    if l1ll1l11l_opy_ == l1ll11ll1_opy_:
        return l1l11_opy_ (u"ࠪࡪࡺࡺࡵࡳࡧࠪࢋ")
    if l1ll1l11l_opy_ == l1llll1l1_opy_:
        return l1l11_opy_ (u"ࠫࡸࡺࡥࡢ࡮ࡷ࡬ࠬࢌ")
def l111l111_opy_(l1ll1l11l_opy_):
    l1llll11l_opy_ = (l1l11_opy_ (u"ࠬࢁࠢ࡫ࡵࡲࡲࡷࡶࡣࠣ࠼ࠥ࠶࠳࠶ࠢ࠭ࠢࠥࡱࡪࡺࡨࡰࡦࠥ࠾ࠧࡌࡩ࡭ࡧࡶ࠲ࡌ࡫ࡴࡅ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠥ࠰ࠥࠨࡰࡢࡴࡤࡱࡸࠨ࠺ࡼࠤࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧࡀࠢࠦࡵࠥࢁ࠱ࠦࠢࡪࡦࠥ࠾ࠥ࠷ࡽࠨࢍ") % l1ll1l11l_opy_)
    if l1ll1l11l_opy_ == l1llll1l1_opy_:
        l1ll111l1_opy_ = l1l11_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳࡀ࠯࠰ࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡴࡶࡨࡥࡱࡺࡨࡶࡰࡧࡩࡷ࡭ࡲࡰࡷࡱࡨ࠴ࡅ࡭ࡰࡦࡨࡁ࡬࡫࡮ࡳࡧࡶࠪࡵࡵࡲࡵࡣ࡯ࡁࠪ࠽ࡢࠦ࠴࠵ࡲࡦࡳࡥࠦ࠴࠵ࠩ࠸ࡧࠥ࠳࠲ࠨ࠶࠷ࠫ࠵ࡣࡋࠨ࠹ࡩࠫ࠵ࡣࡅࡒࡐࡔࡘࠥ࠳࠲ࡺ࡬࡮ࡺࡥࠦ࠷ࡧࡇࡱ࡯ࡣ࡬ࠧ࠵࠴࡙ࡵࠥ࠳࠲࡙࡭ࡪࡽࠥ࠳࠲ࡗ࡬ࡪࠫ࠲࠱ࡎ࡬ࡷࡹࠫ࠲࠱ࡑࡩࠩ࠷࠶ࡃࡩࡣࡱࡲࡪࡲࡳࠦ࠷ࡥࠩ࠷࡬ࡃࡐࡎࡒࡖࠪ࠻ࡤࠦ࠷ࡥࠩ࠷࡬ࡉࠦ࠷ࡧࠩ࠷࠸ࠥ࠳ࡥࠨ࠶࠵ࠫ࠲࠳ࡲࡤࡶࡪࡴࡴࡢ࡮ࠨ࠶࠷ࠫ࠳ࡢࠧ࠵࠴ࠪ࠸࠲ࡧࡣ࡯ࡷࡪࠫ࠲࠳ࠧ࠵ࡧࠪ࠸࠰ࠦ࠴࠵ࡹࡷࡲࠥ࠳࠴ࠨ࠷ࡦࠫ࠲࠱ࠧ࠵࠶࡭ࡺࡴࡱࠧ࠶ࡥࠪ࠸ࡦࠦ࠴ࡩࡱࡼ࠷࠮ࡪࡲࡷࡺ࠻࠼࠮ࡵࡸࠨ࠶࠷ࠫ࠲ࡤࠧ࠵࠴ࠪ࠸࠲ࡱࡲࡤࡷࡸࡽ࡯ࡳࡦࠨ࠶࠷ࠫ࠳ࡢࠧ࠵࠴ࠪ࠸࠲࠱࠲࠳࠴ࠪ࠸࠲ࠦ࠴ࡦࠩ࠷࠶ࠥ࠳࠴ࡰࡥࡨࠫ࠲࠳ࠧ࠶ࡥࠪ࠸࠰ࠦ࠴࠵࠴࠵ࠫ࠳ࡢ࠳ࡄࠩ࠸ࡧ࠷࠹ࠧ࠶ࡥ࠹࠹ࠥ࠴ࡣ࠴࠶ࠪ࠹ࡡ࠸࠶ࠨ࠶࠷ࠫ࠲ࡤࠧ࠵࠴ࠪ࠸࠲ࡴࡧࡵ࡭ࡦࡲࠥ࠳࠴ࠨ࠷ࡦࠫ࠲࠱ࠧ࠺ࡦࠪ࠸࠲ࡴࡧࡱࡨࡤࡹࡥࡳ࡫ࡤࡰࠪ࠸࠲ࠦ࠵ࡤࠩ࠷࠶ࡴࡳࡷࡨࠩ࠷ࡩࠥ࠳࠲ࠨ࠶࠷ࡩࡵࡴࡶࡲࡱࠪ࠸࠲ࠦ࠵ࡤࠩ࠷࠶ࡴࡳࡷࡨࠩ࠷ࡩࠥ࠳࠲ࠨ࠶࠷ࡹ࡮ࠦ࠴࠵ࠩ࠸ࡧࠥ࠳࠲ࠨ࠶࠷ࠫ࠲࠳ࠧ࠵ࡧࠪ࠸࠰ࠦ࠴࠵ࡷ࡮࡭࡮ࡢࡶࡸࡶࡪࠫ࠲࠳ࠧ࠶ࡥࠪ࠸࠰ࠦ࠴࠵ࠩ࠷࠸ࠥ࠳ࡥࠨ࠶࠵ࠫ࠲࠳ࡦࡨࡺ࡮ࡩࡥࡠ࡫ࡧ࠶ࠪ࠸࠲ࠦ࠵ࡤࠩ࠷࠶ࠥ࠳࠴ࠨ࠶࠷ࠫ࠲ࡤࠧ࠵࠴ࠪ࠸࠲ࡥࡧࡹ࡭ࡨ࡫࡟ࡪࡦࠨ࠶࠷ࠫ࠳ࡢࠧ࠵࠴ࠪ࠸࠲ࠦ࠴࠵ࠩ࠼ࡪࠥ࠳ࡥࠨ࠶࠵ࠫ࠲࠳ࡲࡤࡷࡸࡽ࡯ࡳࡦࠨ࠶࠷ࠫ࠳ࡢࠧ࠵࠴ࡳࡻ࡬࡭ࠧ࠵ࡧࠪ࠸࠰ࠦ࠴࠵ࡰࡴ࡭ࡩ࡯ࠧ࠵࠶ࠪ࠹ࡡࠦ࠴࠳ࡲࡺࡲ࡬ࠦ࠹ࡧࠫࢎ")
    else:
        l1ll111l1_opy_ = l1l11_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠺࠰࠱ࠪ࢏") + l1ll1l11l_opy_ + l1l11_opy_ (u"ࠨ࠱ࡂࡥࡨࡺࡩࡰࡰࡀࡷࡪࡩࡵࡳ࡫ࡷࡽࡤࡩࡨࡦࡥ࡮ࠪࡪࡾࡴࡳࡣࠩࡴࡦ࡭ࡥࠧࡲ࡯ࡳࡹࠬࡴࡩࡷࡰࡦࡳࡧࡩ࡭ࠨࡷ࡭ࡹࡲࡥ࠾ࡎ࡬ࡺࡪࠫ࠲࠱ࡖ࡙ࠪࡺࡸ࡬ࠨ࢐")
    query = l1lll11l1_opy_(l1ll1l11l_opy_)
    l1lllllll_opy_ = (l1l11_opy_ (u"ࠩࡾࠦ࡯ࡹ࡯࡯ࡴࡳࡧࠧࡀࠢ࠳࠰࠳ࠦ࠱ࠦࠢ࡮ࡧࡷ࡬ࡴࡪࠢ࠻ࠤࡉ࡭ࡱ࡫ࡳ࠯ࡉࡨࡸࡉ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠭ࠢࠥࡴࡦࡸࡡ࡮ࡵࠥ࠾ࢀࠨࡤࡪࡴࡨࡧࡹࡵࡲࡺࠤ࠽ࠦࠪࡹࠢࡾ࠮ࠣࠦ࡮ࡪࠢ࠻ࠢ࠴ࢁࠬ࢑") % l1ll111l1_opy_)
    l11111ll_opy_ = (l1l11_opy_ (u"ࠪࡿࠧࡰࡳࡰࡰࡵࡴࡨࠨ࠺ࠣ࠴࠱࠴ࠧ࠲ࠠࠣ࡯ࡨࡸ࡭ࡵࡤࠣ࠼ࠥࡊ࡮ࡲࡥࡴ࠰ࡊࡩࡹࡊࡩࡳࡧࡦࡸࡴࡸࡹࠣ࠮ࠣࠦࡵࡧࡲࡢ࡯ࡶࠦ࠿ࢁࠢࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠥ࠾ࠧࠫࡳࠣࡿ࠯ࠤࠧ࡯ࡤࠣ࠼ࠣ࠵ࢂ࠭࢒") % query)
    try:
        xbmc.executeJSONRPC(l1llll11l_opy_)
        xbmc.executeJSONRPC(l1lllllll_opy_)
        response = xbmc.executeJSONRPC(l11111ll_opy_)
        content  = json.loads(response.decode(l1l11_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪ࢓"), l1l11_opy_ (u"ࠬ࡯ࡧ࡯ࡱࡵࡩࠬ࢔")))
        return content
    except KeyError:
        tardis.log(l1l11_opy_ (u"࠭࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭ࠡࡒ࡯ࡹ࡬࡯࡮ࠡࡇࡵࡶࡴࡸࠠ࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮ࠩ࢕"))
        return {l1l11_opy_ (u"ࠧࡆࡴࡵࡳࡷ࠭࢖") : l1l11_opy_ (u"ࠨࡒ࡯ࡹ࡬࡯࡮ࠡࡇࡵࡶࡴࡸࠧࢗ")}
def l1lll11l1_opy_(l1ll1l11l_opy_):
    if l1ll1l11l_opy_ == l1ll11l11_opy_:
        return l1l11_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠼࠲࠳ࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡵࡺ࡯ࡣ࡬࡫ࡳࡸࡻ࠵࠿ࡢࡥࡷ࡭ࡴࡴ࠽ࡴࡶࡵࡩࡦࡳ࡟ࡷ࡫ࡧࡩࡴࠬࡥࡹࡶࡵࡥࠫࡶࡡࡨࡧࠩࡴࡱࡵࡴࠧࡶ࡫ࡹࡲࡨ࡮ࡢ࡫࡯ࡁࠫࡺࡩࡵ࡮ࡨࡁࡆࡲ࡬ࠧࡷࡵࡰࡂ࠶ࠧ࢘")
    if l1ll1l11l_opy_ == l1ll11ll1_opy_:
        return l1l11_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠽࠳࠴ࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲࡫ࡻࡴࡶࡴࡨࡷࡹࡸࡥࡢ࡯ࡶ࠳ࡄࡧࡣࡵ࡫ࡲࡲࡂࡹࡴࡳࡧࡤࡱࡤࡼࡩࡥࡧࡲࠪࡪࡾࡴࡳࡣࠩࡴࡦ࡭ࡥࠧࡲ࡯ࡳࡹࠬࡴࡩࡷࡰࡦࡳࡧࡩ࡭࠿ࠩࡸ࡮ࡺ࡬ࡦ࠿ࡄࡰࡱࠬࡵࡳ࡮ࡀ࠴࢙ࠬ")
    if l1ll1l11l_opy_ == l1llll1l1_opy_:
        return l1l11_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠾࠴࠵ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡹࡴࡦࡣ࡯ࡸ࡭ࡻ࡮ࡥࡧࡵ࡫ࡷࡵࡵ࡯ࡦ࠲ࡃ࡬࡫࡮ࡳࡧࡢࡲࡦࡳࡥ࠾ࡃ࡯ࡰࠫࡶ࡯ࡳࡶࡤࡰࡂࠫ࠷ࡃࠧ࠵࠶ࡳࡧ࡭ࡦࠧ࠵࠶ࠪ࠹ࡁࠬࠧ࠵࠶ࠪ࠻ࡂࡊࠧ࠸ࡈࠪ࠻ࡂࡄࡑࡏࡓࡗ࠱ࡷࡩ࡫ࡷࡩࠪ࠻ࡄࡄ࡮࡬ࡧࡰ࠱ࡔࡰ࡙࠭࡭ࡪࡽࠫࡕࡪࡨ࠯ࡑ࡯ࡳࡵ࠭ࡒࡪ࠰ࡉࡨࡢࡰࡱࡩࡱࡹࠥ࠶ࡄࠨ࠶ࡋࡉࡏࡍࡑࡕࠩ࠺ࡊࠥ࠶ࡄࠨ࠶ࡋࡏࠥ࠶ࡆࠨ࠶࠷ࠫ࠲ࡄ࠭ࠨ࠶࠷ࡶࡡࡳࡧࡱࡸࡦࡲࠥ࠳࠴ࠨ࠷ࡆ࠱ࠥ࠳࠴ࡩࡥࡱࡹࡥࠦ࠴࠵ࠩ࠷ࡉࠫࠦ࠴࠵ࡹࡷࡲࠥ࠳࠴ࠨ࠷ࡆ࠱ࠥ࠳࠴࡫ࡸࡹࡶࠥ࠴ࡃࠨ࠶ࡋࠫ࠲ࡇ࡯ࡺ࠵࠳࡯ࡰࡵࡸ࠹࠺࠳ࡺࡶࠦ࠴࠵ࠩ࠷ࡉࠫࠦ࠴࠵ࡴࡵࡧࡳࡴࡹࡲࡶࡩࠫ࠲࠳ࠧ࠶ࡅ࠰ࠫ࠲࠳࠲࠳࠴࠵ࠫ࠲࠳ࠧ࠵ࡇ࠰ࠫ࠲࠳࡯ࡤࡧࠪ࠸࠲ࠦ࠵ࡄ࠯ࠪ࠸࠲࠱࠲ࠨ࠷ࡆ࠷ࡁࠦ࠵ࡄ࠻࠽ࠫ࠳ࡂ࠶࠶ࠩ࠸ࡇ࠱࠳ࠧ࠶ࡅ࠼࠺ࠥ࠳࠴ࠨ࠶ࡈ࠱ࠥ࠳࠴ࡶࡩࡷ࡯ࡡ࡭ࠧ࠵࠶ࠪ࠹ࡁࠬࠧ࠺ࡆࠪ࠸࠲ࡴࡧࡱࡨࡤࡹࡥࡳ࡫ࡤࡰࠪ࠸࠲ࠦ࠵ࡄ࠯ࡹࡸࡵࡦࠧ࠵ࡇ࠰ࠫ࠲࠳ࡥࡸࡷࡹࡵ࡭ࠦ࠴࠵ࠩ࠸ࡇࠫࡵࡴࡸࡩࠪ࠸ࡃࠬࠧ࠵࠶ࡸࡴࠥ࠳࠴ࠨ࠷ࡆ࠱ࠥ࠳࠴ࠨ࠶࠷ࠫ࠲ࡄ࠭ࠨ࠶࠷ࡹࡩࡨࡰࡤࡸࡺࡸࡥࠦ࠴࠵ࠩ࠸ࡇࠫࠦ࠴࠵ࠩ࠷࠸ࠥ࠳ࡅ࠮ࠩ࠷࠸ࡤࡦࡸ࡬ࡧࡪࡥࡩࡥ࠴ࠨ࠶࠷ࠫ࠳ࡂ࠭ࠨ࠶࠷ࠫ࠲࠳ࠧ࠵ࡇ࠰ࠫ࠲࠳ࡦࡨࡺ࡮ࡩࡥࡠ࡫ࡧࠩ࠷࠸ࠥ࠴ࡃ࠮ࠩ࠷࠸ࠥ࠳࠴ࠨ࠻ࡉࠫ࠲ࡄ࠭ࠨ࠶࠷ࡶࡡࡴࡵࡺࡳࡷࡪࠥ࠳࠴ࠨ࠷ࡆ࠱࡮ࡶ࡮࡯ࠩ࠷ࡉࠫࠦ࠴࠵ࡰࡴ࡭ࡩ࡯ࠧ࠵࠶ࠪ࠹ࡁࠬࡰࡸࡰࡱࠫ࠷ࡅࠨࡰࡳࡩ࡫࠽ࡤࡪࡤࡲࡳ࡫࡬ࡴࠨࡪࡩࡳࡸࡥࡠ࡫ࡧࡁࠪ࠸ࡁࠨ࢚")
    else:
        Addon = xbmcaddon.Addon(l1ll1l11l_opy_)
        username =  Addon.getSetting(l1l11_opy_ (u"ࠬࡱࡡࡴࡷࡷࡥ࡯ࡧ࡮ࡪ࡯࡬࢛ࠫ"))
        password =  Addon.getSetting(l1l11_opy_ (u"࠭ࡳࡢ࡮ࡤࡷࡴࡴࡡࠨ࢜"))
        l1ll1l1ll_opy_     = l1l11_opy_ (u"ࠧ࠰ࡁࡤࡧࡹ࡯࡯࡯࠿ࡶࡸࡷ࡫ࡡ࡮ࡡࡹ࡭ࡩ࡫࡯ࠧࡧࡻࡸࡷࡧࠦࡱࡣࡪࡩࠫࡶ࡬ࡰࡶࠩࡸ࡭ࡻ࡭ࡣࡰࡤ࡭ࡱࡃࠦࡵ࡫ࡷࡰࡪࡃࡁ࡭࡮ࠩࡹࡷࡲ࠽ࠨ࢝")
        l1ll111ll_opy_  =  l1111lll_opy_(l1ll1l11l_opy_)
        l1ll11lll_opy_   = l1l11_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠻࠱࠲ࠫ࢞") + l1ll1l11l_opy_
        l1111l1l_opy_  =  l1ll11lll_opy_ + l1ll1l1ll_opy_ + l1ll111ll_opy_
        l1111ll1_opy_ = l1l11_opy_ (u"ࠩࡸࡷࡪࡸ࡮ࡢ࡯ࡨࡁࠬ࢟") + username + l1l11_opy_ (u"ࠪࠪࡵࡧࡳࡴࡹࡲࡶࡩࡃࠧࢠ") + password + l1l11_opy_ (u"ࠫࠫࡺࡹࡱࡧࡀ࡫ࡪࡺ࡟࡭࡫ࡹࡩࡤࡹࡴࡳࡧࡤࡱࡸࠬࡣࡢࡶࡢ࡭ࡩࡃ࠰ࠨࢡ")
        return l1111l1l_opy_ + urllib.quote_plus(l1111ll1_opy_)
def l1111lll_opy_(l1ll1l11l_opy_):
    if (l1ll1l11l_opy_ == l1llll1ll_opy_) or (l1ll1l11l_opy_ == l1lll1111_opy_):
        return l1l11_opy_ (u"ࠬ࡮ࡴࡵࡲ࠽࠳࠴࠹࠷࠯࠳࠻࠻࠳࠷࠳࠺࠰࠴࠹࠺ࡀ࠸࠱࠲࠳࠳ࡪࡴࡩࡨ࡯ࡤ࠶࠳ࡶࡨࡱࡁࠪࢢ")
    if l1ll1l11l_opy_ == l1llll111_opy_:
        return l1l11_opy_ (u"࠭ࡨࡵࡶࡳ࠾࠴࠵࠲࠯ࡹࡨࡰࡨࡳ࠮ࡵࡸ࠽࠼࠵࠶࠰࠰ࡧࡱ࡭࡬ࡳࡡ࠳࠰ࡳ࡬ࡵࡅࠧࢣ")
    if l1ll1l11l_opy_ == l1ll1lll1_opy_:
        return l1l11_opy_ (u"ࠧࡩࡶࡷࡴ࠿࠵࠯࠲࠷࠻࠲࠻࠿࠮࠶࠶࠱࠹࠹ࡀ࠸࠱࠲࠳࠳ࡪࡴࡩࡨ࡯ࡤ࠶࠳ࡶࡨࡱࡁࠪࢤ")
def l1ll1ll11_opy_(l1ll1l11l_opy_, l1111111_opy_):
    if (l1ll1l11l_opy_ == l1llll1ll_opy_) or (l1ll1l11l_opy_ == l1lll1111_opy_) or (l1ll1l11l_opy_ == l1llll111_opy_):
        l1111111_opy_ = l1111111_opy_.replace(l1l11_opy_ (u"ࠨࠢࠣࠫࢥ"), l1l11_opy_ (u"ࠩࠣࠫࢦ")).replace(l1l11_opy_ (u"ࠪࠤࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭ࢧ"), l1l11_opy_ (u"ࠫࡠ࠵ࡃࡐࡎࡒࡖࡢ࠭ࢨ"))
        return l1111111_opy_
    if l1ll1l11l_opy_ == l1ll1lll1_opy_:
        l1111111_opy_ = l1111111_opy_.replace(l1l11_opy_ (u"ࠬࠦࠠࠨࢩ"), l1l11_opy_ (u"࠭ࠠࠨࢪ")).replace(l1l11_opy_ (u"ࠧࠡ࡝࠲ࡆࡢ࠭ࢫ"), l1l11_opy_ (u"ࠨ࡝࠲ࡆࡢ࠭ࢬ"))
        return l1111111_opy_
    if (l1ll1l11l_opy_ == l1ll11l11_opy_) or (l1ll1l11l_opy_ == l1ll11ll1_opy_) or (l1ll1l11l_opy_ == l1llll1l1_opy_):
        return l1111111_opy_
def l1ll1ll1l_opy_(l1ll1l11l_opy_, l1ll1llll_opy_):
    if (l1ll1l11l_opy_ == l1llll1ll_opy_) or (l1ll1l11l_opy_ == l1lll1111_opy_) or (l1ll1l11l_opy_ == l1llll111_opy_):
        channel = l1ll1llll_opy_.rsplit(l1l11_opy_ (u"ࠩ࡞࠳ࡈࡕࡌࡐࡔࡠࠫࢭ"), 1)[0].split(l1l11_opy_ (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡻ࡭࡯ࡴࡦ࡟ࠪࢮ"), 1)[-1]
        channel = channel.replace(l1l11_opy_ (u"ࠫࡇࡈࡃࠡ࠳ࠪࢯ"), l1l11_opy_ (u"ࠬࡈࡂࡄࠢࡒࡲࡪ࠭ࢰ")).replace(l1l11_opy_ (u"࠭ࡂࡃࡅࠣ࠶ࠬࢱ"), l1l11_opy_ (u"ࠧࡃࡄࡆࠤ࡙ࡽ࡯ࠨࢲ")).replace(l1l11_opy_ (u"ࠨࡄࡅࡇࠥ࠺ࠧࢳ"), l1l11_opy_ (u"ࠩࡅࡆࡈࠦࡆࡐࡗࡕࠫࢴ")).replace(l1l11_opy_ (u"ࠪࡍ࡙࡜ࠠ࠲ࠩࢵ"), l1l11_opy_ (u"ࠫࡎ࡚ࡖ࠲ࠩࢶ")).replace(l1l11_opy_ (u"ࠬࡏࡔࡗࠢ࠵ࠫࢷ"), l1l11_opy_ (u"࠭ࡉࡕࡘ࠵ࠫࢸ")).replace(l1l11_opy_ (u"ࠧࡊࡖ࡙ࠤ࠸࠭ࢹ"), l1l11_opy_ (u"ࠨࡋࡗ࡚࠸࠭ࢺ")).replace(l1l11_opy_ (u"ࠩࡌࡘ࡛ࠦ࠴ࠨࢻ"), l1l11_opy_ (u"ࠪࡍ࡙࡜࠴ࠨࢼ"))
        return channel
    if (l1ll1l11l_opy_ == l1ll1lll1_opy_) or (l1ll1l11l_opy_ == l1ll11l11_opy_) or (l1ll1l11l_opy_ == l1ll11ll1_opy_):
        channel = l1ll1llll_opy_.rsplit(l1l11_opy_ (u"ࠫࠥࡡ࠯ࡄࡑࡏࡓࡗࡣࠧࢽ"))[0].replace(l1l11_opy_ (u"ࠬࡡࡃࡐࡎࡒࡖࠥࡽࡨࡪࡶࡨࡡࠬࢾ"), l1l11_opy_ (u"࠭ࠧࢿ"))
        channel = channel.replace(l1l11_opy_ (u"ࠧ࠻ࠩࣀ"), l1l11_opy_ (u"ࠨࠩࣁ")).replace(l1l11_opy_ (u"ࠩࡅࡆࡈࠦ࠱ࠨࣂ"), l1l11_opy_ (u"ࠪࡆࡇࡉࠠࡐࡰࡨࠫࣃ")).replace(l1l11_opy_ (u"ࠫࡇࡈࡃࠡ࠴ࠪࣄ"), l1l11_opy_ (u"ࠬࡈࡂࡄࠢࡗࡻࡴ࠭ࣅ")).replace(l1l11_opy_ (u"࠭ࡂࡃࡅࠣ࠸ࠬࣆ"), l1l11_opy_ (u"ࠧࡃࡄࡆࠤࡋࡕࡕࡓࠩࣇ")).replace(l1l11_opy_ (u"ࠨࡋࡗ࡚ࠥ࠷ࠧࣈ"), l1l11_opy_ (u"ࠩࡌࡘ࡛࠷ࠧࣉ")).replace(l1l11_opy_ (u"ࠪࡍ࡙࡜ࠠ࠳ࠩ࣊"), l1l11_opy_ (u"ࠫࡎ࡚ࡖ࠳ࠩ࣋")).replace(l1l11_opy_ (u"ࠬࡏࡔࡗࠢ࠶ࠫ࣌"), l1l11_opy_ (u"࠭ࡉࡕࡘ࠶ࠫ࣍")).replace(l1l11_opy_ (u"ࠧࡊࡖ࡙ࠤ࠹࠭࣎"), l1l11_opy_ (u"ࠨࡋࡗ࡚࠹࣏࠭"))
        return channel
    else:
        channel = l1ll1llll_opy_.replace(l1l11_opy_ (u"ࠩࡅࡆࡈࠦ࠱ࠨ࣐"), l1l11_opy_ (u"ࠪࡆࡇࡉࠠࡐࡰࡨ࣑ࠫ")).replace(l1l11_opy_ (u"ࠫࡇࡈࡃࠡ࠴࣒ࠪ"), l1l11_opy_ (u"ࠬࡈࡂࡄࠢࡗࡻࡴ࣓࠭")).replace(l1l11_opy_ (u"࠭ࡂࡃࡅࠣ࠸ࠬࣔ"), l1l11_opy_ (u"ࠧࡃࡄࡆࠤࡋࡕࡕࡓࠩࣕ")).replace(l1l11_opy_ (u"ࠨࡋࡗ࡚ࠥ࠷ࠧࣖ"), l1l11_opy_ (u"ࠩࡌࡘ࡛࠷ࠧࣗ")).replace(l1l11_opy_ (u"ࠪࡍ࡙࡜ࠠ࠳ࠩࣘ"), l1l11_opy_ (u"ࠫࡎ࡚ࡖ࠳ࠩࣙ")).replace(l1l11_opy_ (u"ࠬࡏࡔࡗࠢ࠶ࠫࣚ"), l1l11_opy_ (u"࠭ࡉࡕࡘ࠶ࠫࣛ")).replace(l1l11_opy_ (u"ࠧࡊࡖ࡙ࠤ࠹࠭ࣜ"), l1l11_opy_ (u"ࠨࡋࡗ࡚࠹࠭ࣝ"))
        return channel
def l1ll1l1l1_opy_(e):
    l1lllll11_opy_ = l1l11_opy_ (u"ࠩࡖࡳࡷࡸࡹ࠭ࠢࡤࡲࠥ࡫ࡲࡳࡱࡵࠤࡴࡩࡣࡶࡴࡨࡨ࠿ࠦࡊࡔࡑࡑࠤࡊࡸࡲࡰࡴ࠽ࠤࠪࡹࠧࣞ")  %e
    l1lllll1l_opy_ = l1l11_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣࡧࡴࡴࡴࡢࡥࡷࠤࡺࡹࠠࡰࡰࠣࡸ࡭࡫ࠠࡧࡱࡵࡹࡲ࠴ࠧࣟ")
    l1llllll1_opy_ = l1l11_opy_ (u"࡚ࠫࡶ࡬ࡰࡣࡧࠤࡦࠦ࡬ࡰࡩࠣࡺ࡮ࡧࠠࡵࡪࡨࠤࡦࡪࡤࡰࡰࠣࡷࡪࡺࡴࡪࡰࡪࡷࠥࡧ࡮ࡥࠢࡳࡳࡸࡺࠠࡵࡪࡨࠤࡱ࡯࡮࡬࠰ࠪ࣠")
    tardis.log(e)
    tardis.DialogOK(l1lllll11_opy_, l1lllll1l_opy_, l1llllll1_opy_)
    tardis.SetSetting(SETTING, l1l11_opy_ (u"ࠬ࠭࣡"))