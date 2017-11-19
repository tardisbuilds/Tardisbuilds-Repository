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
import xbmcgui
import json
import os
import shutil
import tardis
l1ll11ll1_opy_    = l1l11_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮࡯ࡶࡹࠫ࡟")
l1lll1lll_opy_    = l1l11_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡷ࡮ࡸࡺࡸ࡫ࠨࡠ")
locked = l1l11_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰࡯ࡳࡨࡱࡥࡥࡶࡹࠫࡡ")
l1111ll1_opy_   = l1l11_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡷࡹࡸࡥࡢ࡯ࡷࡺࡧࡵࡸࠨࡢ")
l1llll11l_opy_     = l1l11_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡸࡶ࡯ࡳࡶࡶࡱࡦࡴࡩࡢࠩࡣ")
l11111ll_opy_     = l1l11_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡹࡰࡰࡴࡷࡷࡳࡧࡴࡪࡱࡱ࡬ࡩࡺࡶࠨࡤ")
l1l1ll1ll_opy_     = l1l11_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡵ࡭ࡶ࡬ࡱࡦࡺࡥ࡮ࡣࡱ࡭ࡦ࠭ࡥ")
l1ll11l1l_opy_   = l1l11_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮࡭࡫ࡸࡼ࠳ࡺࡶࠨࡦ")
l1ll111l1_opy_    = l1l11_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡆࡆࡗࡵࡵࡲࡵࡵࠪࡧ")
l1lll1l1l_opy_ = l1l11_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡵࡩࡧࡵ࡯ࡵࠩࡨ")
l1ll111ll_opy_    = l1l11_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡧࡱࡻࡩࡱࡶࡹࠫࡩ")
l1ll11lll_opy_ = l1l11_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡸࡺࡲࡦࡣࡰࡷࡪࡧࡳࡺ࠰ࡷࡺࠬࡪ")
l1lll1111_opy_ = l1l11_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡸࡵࡺࡣ࡬ࡴࡹࡼࠧ࡫")
l1l1l1ll1_opy_ = [l1ll11ll1_opy_, locked, l1ll11l1l_opy_, l1ll11lll_opy_]
HOME = tardis.PROFILE
PATH = os.path.join(HOME, l1l11_opy_ (u"ࠧࡪࡰ࡬ࠫ࡬"))

def checkAddons():
    for addon in l1l1l1ll1_opy_:
        if l1l1ll111_opy_(addon):
            try:
                createINI(addon)
            except: pass
def l1l1ll111_opy_(addon):
    if xbmc.getCondVisibility(l1l11_opy_ (u"ࠩࡖࡽࡸࡺࡥ࡮࠰ࡋࡥࡸࡇࡤࡥࡱࡱࠬࠪࡹࠩࠨ࡮") % addon) == 1:
        return True
    return False
def createINI(addon):
    l1111l1l_opy_ = str(addon).split(l1l11_opy_ (u"ࠪ࠲ࠬ࡯"))[2] + l1l11_opy_ (u"ࠫ࠳࡯࡮ࡪࠩࡰ")
    l1ll1lll1_opy_  = os.path.join(PATH, l1111l1l_opy_)
    try:
        l111111l_opy_ = l111l111_opy_(addon)
    except KeyError:
        tardis.log(l1l11_opy_ (u"ࠬ࠳࠭࠮࠯࠰ࠤࡐ࡫ࡹࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡪࡩࡹࡌࡩ࡭ࡧࡶࠤ࠲࠳࠭࠮࠯ࠣࠫࡱ") + addon)
        result = {l1l11_opy_ (u"ࡻࠧࡧ࡫࡯ࡩࡸ࠭ࡲ"): [{l1l11_opy_ (u"ࡵࠨࡨ࡬ࡰࡪࡺࡹࡱࡧࠪࡳ"): l1l11_opy_ (u"ࡶࠩࡩ࡭ࡱ࡫ࠧࡴ"), l1l11_opy_ (u"ࡷࠪࡸࡾࡶࡥࠨࡵ"): l1l11_opy_ (u"ࡸࠫࡺࡴ࡫࡯ࡱࡺࡲࠬࡶ"), l1l11_opy_ (u"ࡹࠬ࡬ࡩ࡭ࡧࠪࡷ"): l1l11_opy_ (u"ࡺ࠭ࡰ࡭ࡷࡪ࡭ࡳࡀ࠯࠰ࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡹࡺࡻࠫࡸ"), l1l11_opy_ (u"ࡻࠧ࡭ࡣࡥࡩࡱ࠭ࡹ"): l1l11_opy_ (u"ࡵࠨࡐࡒࠤࡈࡎࡁࡏࡐࡈࡐࡘ࠭ࡺ")}], l1l11_opy_ (u"ࡶࠩ࡯࡭ࡲ࡯ࡴࡴࠩࡻ"):{l1l11_opy_ (u"ࡷࠪࡷࡹࡧࡲࡵࠩࡼ"): 0, l1l11_opy_ (u"ࡸࠫࡹࡵࡴࡢ࡮ࠪࡽ"): 1, l1l11_opy_ (u"ࡹࠬ࡫࡮ࡥࠩࡾ"): 1}}
    l1l1lllll_opy_  = file(l1ll1lll1_opy_, l1l11_opy_ (u"ࠬࡽࠧࡿ"))
    l1l1lllll_opy_.write(l1l11_opy_ (u"࡛࠭ࠨࢀ"))
    l1l1lllll_opy_.write(addon)
    l1l1lllll_opy_.write(l1l11_opy_ (u"ࠧ࡞ࠩࢁ"))
    l1l1lllll_opy_.write(l1l11_opy_ (u"ࠨ࡞ࡱࠫࢂ"))
    l1ll1l1l1_opy_ = []
    for channel in l111111l_opy_:
        l1lll11ll_opy_    = channel[l1l11_opy_ (u"ࠩ࡯ࡥࡧ࡫࡬ࠨࢃ")].replace(l1l11_opy_ (u"ࠪ࡟ࡇࡣ࡛ࡄࡑࡏࡓࡗࠦࡷࡩ࡫ࡷࡩࡢ࠭ࢄ"), l1l11_opy_ (u"ࠫࠬࢅ")).replace(l1l11_opy_ (u"ࠬࡡ࠯ࡄࡑࡏࡓࡗࡣ࡛࠰ࡄࡠࠫࢆ"), l1l11_opy_ (u"࠭ࠧࢇ")).replace(l1l11_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡨࡴࡨࡩࡳࡣࡈࡅ࡝࠲ࡇࡔࡒࡏࡓ࡟ࠪ࢈"), l1l11_opy_ (u"ࠨࡊࡇࡈࠬࢉ"))
        l1lll11ll_opy_    = l1lll11ll_opy_.replace(l1l11_opy_ (u"ࠩࡿࠫࢊ"), l1l11_opy_ (u"ࠪࠫࢋ")).replace(l1l11_opy_ (u"ࠫ࠴࠭ࢌ"), l1l11_opy_ (u"ࠬ࠭ࢍ")).replace(l1l11_opy_ (u"࠭ࠠࠡࠢࠣࠤࠬࢎ"), l1l11_opy_ (u"ࠧࠡࠩ࢏")).replace(l1l11_opy_ (u"ࠨ࠰࠱࠲࠳࠴ࠧ࢐"), l1l11_opy_ (u"ࠩࠪ࢑")).replace(l1l11_opy_ (u"ࠪ࠾ࠬ࢒"), l1l11_opy_ (u"ࠫࠬ࢓"))
        l1lll11ll_opy_    = l1lll11ll_opy_.replace(l1l11_opy_ (u"ࠬࡣࠠࠨ࢔"), l1l11_opy_ (u"࠭࡝ࠨ࢕")).replace(l1l11_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡢࡳࡸࡥࡢ࠭࢖"), l1l11_opy_ (u"ࠨࠩࢗ")).replace(l1l11_opy_ (u"ࠩ࡞ࡇࡔࡒࡏࡓࠢࡺ࡬࡮ࡺࡥ࡞ࠩ࢘"), l1l11_opy_ (u"࢙ࠪࠫ")).replace(l1l11_opy_ (u"ࠫࠥࡡ࢚ࠧ"), l1l11_opy_ (u"ࠬࡡ࢛ࠧ"))
        l1lll11ll_opy_    = l1lll11ll_opy_.replace(l1l11_opy_ (u"࡛࠭ࡄࡑࡏࡓࡗࠦ࡬ࡪ࡯ࡨ࡫ࡷ࡫ࡥ࡯࡟ࠪ࢜"), l1l11_opy_ (u"ࠧࠨ࢝")).replace(l1l11_opy_ (u"ࠨ࡝ࡆࡓࡑࡕࡒࠡࡻࡨࡰࡱࡵࡷ࡞ࠩ࢞"), l1l11_opy_ (u"ࠩࠪ࢟"))
        l1lll11ll_opy_    = l1lll11ll_opy_.replace(l1l11_opy_ (u"ࠪ࡟ࡈࡕࡌࡐࡔࠣࡦࡱࡻࡥ࡞ࠩࢠ"), l1l11_opy_ (u"ࠫࠬࢡ")).replace(l1l11_opy_ (u"ࠬࡡࡃࡐࡎࡒࡖࠥࡵࡲࡢࡰࡪࡩࡢ࠭ࢢ"), l1l11_opy_ (u"࠭ࠧࢣ")).replace(l1l11_opy_ (u"ࠧ࡜ࡅࡒࡐࡔࡘࠠࡳࡧࡧࡡࠬࢤ"), l1l11_opy_ (u"ࠨࠩࢥ"))
        l1lll11ll_opy_    = l1lll11ll_opy_.replace(l1l11_opy_ (u"ࠩ࡞ࡍࡢ࠭ࢦ"), l1l11_opy_ (u"ࠪࠫࢧ")).replace(l1l11_opy_ (u"ࠫࡠ࠵ࡉ࡞ࠩࢨ"), l1l11_opy_ (u"ࠬ࠭ࢩ")).replace(l1l11_opy_ (u"࡛࠭ࡃ࡟ࠪࢪ"), l1l11_opy_ (u"ࠧࠨࢫ")).replace(l1l11_opy_ (u"ࠨ࡝࠲ࡆࡢ࠭ࢬ"), l1l11_opy_ (u"ࠩࠪࢭ"))
        l11111l1_opy_ = tardis.mapChannelName(l1lll11ll_opy_)
        stream   = channel[l1l11_opy_ (u"ࠪࡪ࡮ࡲࡥࠨࢮ")]
        l1llllll1_opy_ = l11111l1_opy_ + l1l11_opy_ (u"ࠫࡂ࠭ࢯ") + stream
        l1ll1l1l1_opy_.append(l1llllll1_opy_)
        l1ll1l1l1_opy_.sort()
    for item in l1ll1l1l1_opy_:
        l1l1lllll_opy_.write(l1l11_opy_ (u"ࠧࠫࡳ࡝ࡰࠥࢰ") % item)
    l1l1lllll_opy_.close()
def l111l111_opy_(addon):
    if addon == l1111111_opy_:
        return l1lll11l1_opy_(addon)
    if addon == l1lll1111_opy_:
        return l11111l1_opy_(addon)
    if addon in [l1ll11ll1_opy_, l1111l1l_opy_, l1ll1l1l1_opy_]:
        return
    try:
        if xbmcaddon.Addon(addon).getSetting(l1l11_opy_ (u"ࠪ࡫ࡪࡴࡲࡦ࢙ࠩ")) == l1l11_opy_ (u"ࠫࡹࡸࡵࡦ࢚ࠩ"):
            xbmcaddon.Addon(addon).setSetting(l1l11_opy_ (u"ࠬ࡭ࡥ࡯ࡴࡨ࢛ࠫ"), l1l11_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬ࢜"))
            xbmcgui.Window(10000).setProperty(l1l11_opy_ (u"ࠧࡑࡎࡘࡋࡎࡔ࡟ࡈࡇࡑࡖࡊ࠭࢝"), l1l11_opy_ (u"ࠨࡖࡵࡹࡪ࠭࢞"))
        if xbmcaddon.Addon(addon).getSetting(l1l11_opy_ (u"ࠩࡷࡺ࡬ࡻࡩࡥࡧࠪ࢟")) == l1l11_opy_ (u"ࠪࡸࡷࡻࡥࠨࢠ"):
            xbmcaddon.Addon(addon).setSetting(l1l11_opy_ (u"ࠫࡹࡼࡧࡶ࡫ࡧࡩࠬࢡ"), l1l11_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫࢢ"))
            xbmcgui.Window(10000).setProperty(l1l11_opy_ (u"࠭ࡐࡍࡗࡊࡍࡓࡥࡔࡗࡉࡘࡍࡉࡋࠧࢣ"), l1l11_opy_ (u"ࠧࡕࡴࡸࡩࠬࢤ"))
    except: pass
    l1ll1ll1l_opy_  = l1l11_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠻࠱࠲ࠫࢥ") + addon
    l1llll1l1_opy_ =  l1111lll_opy_(addon)
    query   =  l1ll1ll1l_opy_ + l1llll1l1_opy_
    return sendJSON(query, addon)
def l1ll1ll11_opy_(addon):
    if addon == l1ll11l1l_opy_:
        l1ll1llll_opy_ = [l1l11_opy_ (u"ࠧ࠶ࠩࢲ"), l1l11_opy_ (u"ࠨ࠳࠳࠺ࠬࢳ"), l1l11_opy_ (u"ࠩ࠷ࠫࢴ"), l1l11_opy_ (u"ࠪ࠶࠻࠹ࠧࢵ"), l1l11_opy_ (u"ࠫ࠶࠹࠲ࠨࢶ")]
    if addon == locked:
        l1ll1llll_opy_ = [l1l11_opy_ (u"ࠬ࠹࠰ࠨࢷ"), l1l11_opy_ (u"࠭࠳࠲ࠩࢸ"), l1l11_opy_ (u"ࠧ࠴࠴ࠪࢹ"), l1l11_opy_ (u"ࠨ࠵࠶ࠫࢺ"), l1l11_opy_ (u"ࠩ࠶࠸ࠬࢻ"), l1l11_opy_ (u"ࠪ࠷࠺࠭ࢼ"), l1l11_opy_ (u"ࠫ࠸࠾ࠧࢽ"), l1l11_opy_ (u"ࠬ࠺࠰ࠨࢾ"), l1l11_opy_ (u"࠭࠴࠲ࠩࢿ"), l1l11_opy_ (u"ࠧ࠵࠷ࠪࣀ"), l1l11_opy_ (u"ࠨ࠶࠺ࠫࣁ"), l1l11_opy_ (u"ࠩ࠷࠽ࠬࣂ"), l1l11_opy_ (u"ࠪ࠹࠷࠭ࣃ")]
    login = l1l11_opy_ (u"ࠫࢀࠨࡪࡴࡱࡱࡶࡵࡩࠢ࠻ࠤ࠵࠲࠵ࠨࠬࠡࠤࡰࡩࡹ࡮࡯ࡥࠤ࠽ࠦࡋ࡯࡬ࡦࡵ࠱ࡋࡪࡺࡄࡪࡴࡨࡧࡹࡵࡲࡺࠤ࠯ࠤࠧࡶࡡࡳࡣࡰࡷࠧࡀࡻࠣࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠦ࠿ࠨࡰ࡭ࡷࡪ࡭ࡳࡀ࠯࠰ࠧࡶ࠳ࠧࢃࠬࠡࠤ࡬ࡨࠧࡀࠠ࠲ࡿࠪࣄ") % addon
    xbmc.executeJSONRPC(login)
    l1ll1ll1l_opy_ = []
    for l1llll111_opy_ in l1ll1llll_opy_:
        if addon == l1ll11l1l_opy_:
            l1lll11l1_opy_ = l1l11_opy_ (u"ࠬࢁࠢ࡫ࡵࡲࡲࡷࡶࡣࠣ࠼ࠥ࠶࠳࠶ࠢ࠭ࠢࠥࡱࡪࡺࡨࡰࡦࠥ࠾ࠧࡌࡩ࡭ࡧࡶ࠲ࡌ࡫ࡴࡅ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠥ࠰ࠥࠨࡰࡢࡴࡤࡱࡸࠨ࠺ࡼࠤࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧࡀࠢࡱ࡮ࡸ࡫࡮ࡴ࠺࠰࠱ࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯࡮࡬ࡹࡽ࠴ࡴࡷ࠱ࡂࡱࡴࡪࡥࡠ࡫ࡧࡁࡨ࡮ࡡ࡯ࡰࡨࡰࡸࠬ࡭ࡰࡦࡨࡁࡨ࡮ࡡ࡯ࡰࡨࡰࡸࠬࡳࡦࡥࡷ࡭ࡴࡴ࡟ࡪࡦࡀࠩࡸࠨࡽ࠭ࠢࠥ࡭ࡩࠨ࠺ࠡ࠳ࢀࠫࣅ") % l1llll111_opy_
        if addon == locked:
            l1lll11l1_opy_ = l1l11_opy_ (u"࠭ࡻࠣ࡬ࡶࡳࡳࡸࡰࡤࠤ࠽ࠦ࠷࠴࠰ࠣ࠮ࠣࠦࡲ࡫ࡴࡩࡱࡧࠦ࠿ࠨࡆࡪ࡮ࡨࡷ࠳ࡍࡥࡵࡆ࡬ࡶࡪࡩࡴࡰࡴࡼࠦ࠱ࠦࠢࡱࡣࡵࡥࡲࡹࠢ࠻ࡽࠥࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠨ࠺ࠣࡲ࡯ࡹ࡬࡯࡮࠻࠱࠲ࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰࡯ࡳࡨࡱࡥࡥࡶࡹ࠳ࡄࡻࡲ࡭࠿ࠨࡷࠫࡳ࡯ࡥࡧࡀ࠸ࠫࡴࡡ࡮ࡧࡀࠪ࡮ࡩ࡯࡯࡫ࡰࡥ࡬࡫࠽ࠧࡲ࡯ࡥࡾࡃࠦࡥࡣࡷࡩࡂࠬࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࡁࠫࡶࡡࡨࡧࡀࠦࢂ࠲ࠠࠣ࡫ࡧࠦ࠿ࠦ࠱ࡾࠩࣆ") % l1llll111_opy_
        l1ll1l111_opy_  = xbmc.executeJSONRPC(l1lll11l1_opy_)
        response = json.loads(l1ll1l111_opy_)
        l1ll1ll1l_opy_.extend(response[l1l11_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧࣇ")][l1l11_opy_ (u"ࠨࡨ࡬ࡰࡪࡹࠧࣈ")])
    return l1ll1ll1l_opy_
def sendJSON(query, addon):
    l1lll11l1_opy_     = l1l11_opy_ (u"ࠩࡾࠦ࡯ࡹ࡯࡯ࡴࡳࡧࠧࡀࠢ࠳࠰࠳ࠦ࠱ࠦࠢ࡮ࡧࡷ࡬ࡴࡪࠢ࠻ࠤࡉ࡭ࡱ࡫ࡳ࠯ࡉࡨࡸࡉ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠭ࠢࠥࡴࡦࡸࡡ࡮ࡵࠥ࠾ࢀࠨࡤࡪࡴࡨࡧࡹࡵࡲࡺࠤ࠽ࠦࠪࡹࠢࡾ࠮ࠣࠦ࡮ࡪࠢ࠻ࠢ࠴ࢁࠬࣉ") % query
    l1ll1l111_opy_  = xbmc.executeJSONRPC(l1lll11l1_opy_)
    response = json.loads(l1ll1l111_opy_)
    result   = response[l1l11_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪ࣊")]
    return result[l1l11_opy_ (u"ࠫ࡫࡯࡬ࡦࡵࠪ࣋")]
def l1ll11l11_opy_(addon):
    l1l1llll1_opy_ = l1l11_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠿࠵࠯ࠨ࣌") + addon
    l1l1l11l1_opy_  = l1l11_opy_ (u"࠭࠿ࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠫ࡯ࡣࡰࡰ࡬ࡱࡦ࡭ࡥ࠾ࡪࡷࡸࡵࠫ࠳ࡢࠧ࠵ࡪࠪ࠸ࡦ࡮ࡧࡷࡥࡱࡱࡥࡵࡶ࡯ࡩ࠳ࡩ࡯ࠦ࠴ࡩ࡙ࡐ࡚ࡵࡳ࡭࠴࠼࠵࠸࠲࠱࠳࠹ࠩ࠷࡬ࡴࡩࡷࡰࡦࡸࠫ࠲ࡧࡰࡨࡻࠪ࠸ࡦࡖ࡭ࠨ࠶࠺࠸࠰ࡵࡷࡵ࡯ࠪ࠸࠵࠳࠲ࡷ࡬ࡺࡳࡢ࡯ࡣ࡬ࡰࡸࠫ࠲࠶࠴࠳ࡰ࡮ࡼࡥࠦ࠴࠸࠶࠵ࡺࡶ࠯࡬ࡳ࡫ࠫࡳ࡯ࡥࡧࡀ࠵ࠫࡴࡡ࡮ࡧࡀࡐ࡮ࡼࡥࠦ࠴࠳ࡘ࡛ࠬࡵࡳ࡮ࡀ࡬ࡹࡺࡰࠦ࠵ࡤࠩ࠷࡬ࠥ࠳ࡨࡰࡩࡹࡧ࡬࡬ࡧࡷࡸࡱ࡫࠮ࡤࡱࠨ࠶࡫࡛ࡋࡕࡷࡵ࡯࠶࠾࠰࠳࠴࠳࠵࠻ࠫ࠲ࡧࡎ࡬ࡺࡪࠫ࠲࠶࠴࠳ࡘ࡛࠴ࡴࡹࡶࠪ࣍")
    l1ll1ll1l_opy_  = []
    l1ll1ll1l_opy_ += sendJSON(l1l1llll1_opy_ + l1l1l11l1_opy_, addon)
    l1ll1ll1l_opy_.sort()
    return l1ll1ll1l_opy_
def l1lllll1l_opy_(addon):
    l1l1llll1_opy_ = l1l11_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠺࠰࠱ࠪ࣎") + addon
    l1l1l11l1_opy_ = l1l11_opy_ (u"ࠨ࠱ࡂࡪࡦࡴࡡࡳࡶࡀ࡬ࡹࡺࡰࠦ࠵ࡤࠩ࠷࡬ࠥ࠳ࡨࡪࡳࡴ࠴ࡧ࡭ࠧ࠵ࡪ࡝ࡪࡆ࠳࠺ࡗࠪࡲࡵࡤࡦ࠿࠴ࠪࡳࡧ࡭ࡦ࠿ࡏ࡭ࡻ࡫ࠥ࠳࠲ࡘࡏࠪ࠸࠰ࡔࡲࡲࡶࡹࡹࠦࡶࡴ࡯ࡁ࡭ࡺࡴࡱࡵࠨ࠷ࡦࠫ࠲ࡧࠧ࠵ࡪ࡬ࡵ࡯࠯ࡩ࡯ࠩ࠷࡬࠵ࡲࡓࡪࡉ࠹࣏࠭")
    l1l1l1l1l_opy_ = l1l11_opy_ (u"ࠩ࠲ࡃ࡫ࡧ࡮ࡢࡴࡷࡁ࡭ࡺࡴࡱࡵࠨ࠷ࡦࠫ࠲ࡧࠧ࠵ࡪ࡬ࡵ࡯࠯ࡩ࡯ࠩ࠷࡬ࡆࡨ࡙ࡐ࡯࡟ࠬ࡭ࡰࡦࡨࡁ࠶ࠬ࡮ࡢ࡯ࡨࡁࡑ࡯ࡶࡦࠧ࠵࠴࡚࡙ࠥ࠳ࡨࡆࡅࡓࠫ࠲࠱ࡕࡳࡳࡷࡺࡳࠧࡷࡵࡰࡂ࡮ࡴࡵࡲࡶࠩ࠸ࡧࠥ࠳ࡨࠨ࠶࡫࡭࡯ࡰ࠰ࡪࡰࠪ࠸ࡦࡧ࠻࡭࡫࠽ࡔ࣐ࠧ")
    l1ll1ll1l_opy_  = []
    l1ll1ll1l_opy_ += sendJSON(l1l1llll1_opy_ + l1l1l11l1_opy_, addon)
    l1ll1ll1l_opy_ += sendJSON(l1l1llll1_opy_ + l1l1l1l1l_opy_, addon)
    return l1ll1ll1l_opy_
def l1111lll_opy_(addon):
    if addon == l1lll11ll_opy_:
        return l1l11_opy_ (u"ࠬ࠵࠿ࡤࡣࡷࡁ࠲࠸ࠦ࡮ࡱࡧࡩࡂ࠸ࠦ࡯ࡣࡰࡩࡂࡓࡹࠦ࠴࠳ࡇ࡭ࡧ࡮࡯ࡧ࡯ࡷࠫࡻࡲ࡭࠿ࡸࡶࡱ࠭ࢰ")
    return l1l11_opy_ (u"࠭ࠧࢱ")
def sendJSON(query, addon):
    try:
        l1llll1ll_opy_     = l1l11_opy_ (u"ࠧࡼࠤ࡭ࡷࡴࡴࡲࡱࡥࠥ࠾ࠧ࠸࠮࠱ࠤ࠯ࠤࠧࡳࡥࡵࡪࡲࡨࠧࡀࠢࡇ࡫࡯ࡩࡸ࠴ࡇࡦࡶࡇ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧ࠲ࠠࠣࡲࡤࡶࡦࡳࡳࠣ࠼ࡾࠦࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠻ࠤࠨࡷࠧࢃࠬࠡࠤ࡬ࡨࠧࡀࠠ࠲ࡿࠪࢲ") % query
        l1lll1l1l_opy_  = xbmc.executeJSONRPC(l1llll1ll_opy_)
        response = json.loads(l1lll1l1l_opy_)
        if xbmcgui.Window(10000).getProperty(l1l11_opy_ (u"ࠨࡒࡏ࡙ࡌࡏࡎࡠࡉࡈࡒࡗࡋࠧࢳ")) == l1l11_opy_ (u"ࠩࡗࡶࡺ࡫ࠧࢴ"):
            xbmcaddon.Addon(addon).setSetting(l1l11_opy_ (u"ࠪ࡫ࡪࡴࡲࡦࠩࢵ"), l1l11_opy_ (u"ࠫࡹࡸࡵࡦࠩࢶ"))
            xbmcgui.Window(10000).clearProperty(l1l11_opy_ (u"ࠬࡖࡌࡖࡉࡌࡒࡤࡍࡅࡏࡔࡈࠫࢷ"))
        if xbmcgui.Window(10000).getProperty(l1l11_opy_ (u"࠭ࡐࡍࡗࡊࡍࡓࡥࡔࡗࡉࡘࡍࡉࡋࠧࢸ")) == l1l11_opy_ (u"ࠧࡕࡴࡸࡩࠬࢹ"):
            xbmcaddon.Addon(addon).setSetting(l1l11_opy_ (u"ࠨࡶࡹ࡫ࡺ࡯ࡤࡦࠩࢺ"), l1l11_opy_ (u"ࠩࡷࡶࡺ࡫ࠧࢻ"))
            xbmcgui.Window(10000).clearProperty(l1l11_opy_ (u"ࠪࡔࡑ࡛ࡇࡊࡐࡢࡘ࡛ࡍࡕࡊࡆࡈࠫࢼ"))
        return response[l1l11_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫࢽ")][l1l11_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡶࠫࢾ")]
    except Exception as e:
        l1ll1llll_opy_(e, addon)
        return {l1l11_opy_ (u"࠭ࡅࡳࡴࡲࡶࠬࢿ") : l1l11_opy_ (u"ࠧࡑ࡮ࡸ࡫࡮ࡴࠠࡆࡴࡵࡳࡷ࠭ࣀ")}
def l1ll1llll_opy_(e, addon):
    l1lllll1l_opy_ = l1l11_opy_ (u"ࠨࡕࡲࡶࡷࡿࠬࠡࡣࡱࠤࡪࡸࡲࡰࡴࠣࡳࡨࡩࡵࡳࡧࡧ࠾ࠥࡐࡓࡐࡐࠣࡉࡷࡸ࡯ࡳ࠼ࠣࠩࡸ࠲ࠠࠦࡵࠪࣁ")  % (e, addon)
    l1llllll1_opy_ = l1l11_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢࡦࡳࡳࡺࡡࡤࡶࠣࡹࡸࠦ࡯࡯ࠢࡷ࡬ࡪࠦࡦࡰࡴࡸࡱ࠳࠭ࣂ")
    l1lllllll_opy_ = l1l11_opy_ (u"࡙ࠪࡵࡲ࡯ࡢࡦࠣࡥࠥࡲ࡯ࡨࠢࡹ࡭ࡦࠦࡴࡩࡧࠣࡥࡩࡪ࡯࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࡶࠤࡦࡴࡤࠡࡲࡲࡷࡹࠦࡴࡩࡧࠣࡰ࡮ࡴ࡫࠯ࠩࣃ")
    tardis.log(addon)
    tardis.log(e)
def getPlaylist():
    import requests
    l1ll1l11l_opy_ = [l1l11_opy_ (u"ࠬ࡮ࡴࡵࡲ࠽࠳࠴ࡾ࠮ࡤࡱ࠲ࡌࡊࡠ࠵࡛ࡻ࡬ࡎࡪ࡝ࠧࣚ"), l1l11_opy_ (u"࠭ࡨࡵࡶࡳ࠾࠴࠵ࡸ࠯ࡥࡲ࠳ࡽ࡬࠵ࡊ࠵ࡋࡓࡩ࡟ࡎࠨࣛ"), l1l11_opy_ (u"ࠧࡩࡶࡷࡴ࠿࠵࠯ࡹ࠰ࡦࡳ࠴࡛ࡌࡤ࠲࠴ࡑࡔࡒࡧࡄࠩࣜ"), l1l11_opy_ (u"ࠨࡪࡷࡸࡵࡀ࠯࠰ࡺ࠱ࡧࡴ࠵ࡪࡶࡐࡐࡒ࡬ࡽࡪࡑ࠲ࠪࣝ"), l1l11_opy_ (u"ࠩ࡫ࡸࡹࡶ࠺࠰࠱ࡻ࠲ࡨࡵ࠯ࡥ࡬ࡅࡥ࠶ࡴࡶ࠺ࡉࡽࠫࣞ"), l1l11_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࡼ࠳ࡩ࡯࠰ࡰ࡙ࡷࡶࡩࡧࡤࡥ࠼ࡽࠬࣟ"), l1l11_opy_ (u"ࠫ࡭ࡺࡴࡱ࠼࠲࠳ࡽ࠴ࡣࡰ࠱ࡻࡐࡈ࠿࠴ࡆࡘࡔࡺ࡞࠭࣠"), l1l11_opy_ (u"ࠬ࡮ࡴࡵࡲ࠽࠳࠴ࡾ࠮ࡤࡱ࠲ࡸࡸࡋ࠳ࡋࡒࡷࡪࡒࡸࠧ࣡"), l1l11_opy_ (u"࠭ࡨࡵࡶࡳ࠾࠴࠵ࡸ࠯ࡥࡲ࠳ࡪ࡜ࡖࡂࡹࡎࡍࡸ࡙ࡨࠨ࣢"), l1l11_opy_ (u"ࠧࡩࡶࡷࡴ࠿࠵࠯ࡹ࠰ࡦࡳ࠴ࡾࡑࡱࡈࡍ࡛࡬࡯ࡧ࡫ࣣࠩ")]
    l1l1lll1l_opy_ =  l1l11_opy_ (u"ࠨࠥࡈ࡜࡙ࡓ࠳ࡖࠩࣤ")
    for url in l1ll1l11l_opy_:
        try:
            request  = requests.get(url)
            l1llll1l1_opy_ = request.text
        except: pass
        if l1l1lll1l_opy_ in l1llll1l1_opy_:
            path = os.path.join(tardis.PROFILE, l1l11_opy_ (u"ࠩࡳࡰࡦࡿ࡬ࡪࡵࡷ࠲ࡲ࠹ࡵࠨࣥ"))
            with open(path, l1l11_opy_ (u"ࠪࡻࣦࠬ")) as f:
                f.write(l1llll1l1_opy_)
                break
def getPluginInfo(streamurl):
    if streamurl.isdigit():
        l1ll1l111_opy_   = l1l11_opy_ (u"ࠫࡐࡵࡤࡪࠢࡓ࡚ࡗࠦࡃࡩࡣࡱࡲࡪࡲࠧ࣋")
        l1ll1l1ll_opy_ = os.path.join(tardis.RESOURCES, l1l11_opy_ (u"ࠬࡱ࡯ࡥ࡫࠰ࡴࡻࡸ࠮ࡱࡰࡪࠫ࣌"))
        return l1ll1l111_opy_, l1ll1l1ll_opy_
    if streamurl.startswith(l1l11_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳࡀ࠯࠰ࠩ࣍")):
        name = streamurl.split(l1l11_opy_ (u"ࠧ࠰࠱ࠪ࣎"), 1)[-1].split(l1l11_opy_ (u"ࠨ࠱࣏ࠪ"), 1)[0]
    if streamurl.startswith(l1l11_opy_ (u"ࠩࡢࡣࡘࡌ࡟ࡠ࣐ࠩ")):
        name = l1l11_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡴࡷࡵࡧࡳࡣࡰ࠲ࡸࡻࡰࡦࡴ࠱ࡪࡦࡼ࡯ࡶࡴ࡬ࡸࡪࡹ࣑ࠧ")
    if streamurl.startswith(l1l11_opy_ (u"ࠫࡍࡊࡔࡗ࠼࣒ࠪ")):
        name = l1l11_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲࡭ࡪࡴࡷ࣓ࠩ")
    if streamurl.startswith(l1l11_opy_ (u"࠭ࡈࡅࡖ࡙࠶࠿࠭ࣔ")):
        name = l1l11_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡲࡶࡻࡤ࡭ࡵࡺࡶࠨࣕ")
    if streamurl.startswith(l1l11_opy_ (u"ࠨࡊࡇࡘ࡛࠹࠺ࠨࣖ")):
        name = l1l11_opy_ (u"ࠩࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡴࡸࡽࡦࡺࡶࠨࣗ")
    if streamurl.startswith(l1l11_opy_ (u"ࠪࡌࡉ࡚ࡖ࠵࠼ࠪࣘ")):
        name = l1l11_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡼࡱ࠭ࣙ")
    if streamurl.startswith(l1l11_opy_ (u"ࠬࡏࡐࡍࡃ࡜࠾ࠬࣚ")):
        name = l1l11_opy_ (u"࠭ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡨࡢࡤ࡫ࡳࡰࡦࡿࡥࡳࠩࣛ")
    if streamurl.startswith(l1l11_opy_ (u"ࠧࡊࡒࡏࡅ࡞࠸࠺ࠨࣜ")):
        name = l1l11_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡪࡲ࡯ࡥࡾ࡫ࡲࡸࡹࡺࠫࣝ")
    if streamurl.startswith(l1l11_opy_ (u"ࠩࡌࡔࡑࡇ࡙ࡓ࠼ࠪࣞ")):
        name = l1l11_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰࡬ࡴࡱࡧࡹࡦࡴࡺࡻࡼ࠭ࣟ")
    if streamurl.startswith(l1l11_opy_ (u"ࠫࡎࡖࡌࡂ࡛ࡌࡘ࡛ࡀࠧ࣠")):
        name = l1l11_opy_ (u"ࠬࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲࡮ࡺࡶࠨ࣡")
    if streamurl.startswith(l1l11_opy_ (u"࠭ࡌࡊࡘࡈࡘ࡛ࡀࠧ࣢")):
        name = l1l11_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴࡬ࡪࡸࡨࡱ࡮ࡾࣣࠧ")
    if streamurl.startswith(l1l11_opy_ (u"ࠨࡷࡳࡲࡵࡀࠧࣤ")):
        name = l1l11_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵ࠰࡫ࡨ࡭ࡵ࡭ࡦࡴࡸࡲ࠳ࡼࡩࡦࡹࠪࣥ")
    try:
        l1ll1l111_opy_   = xbmcaddon.Addon(name).getAddonInfo(l1l11_opy_ (u"ࠪࡲࡦࡳࡥࠨࣦ"))
        l1ll1l1ll_opy_ = xbmcaddon.Addon(name).getAddonInfo(l1l11_opy_ (u"ࠫ࡮ࡩ࡯࡯ࠩࣧ"))

    except:
        l1ll1l111_opy_   = l1l11_opy_ (u"࡛ࠬ࡮࡬ࡰࡲࡻࡳࠦࡳࡵࡴࡨࡥࡲࠦ࡯ࡳࠢࡤࡨࡩ࠳࡯࡯ࠩࣨ")
        l1ll1l1ll_opy_ =  tardis.ICON
    return l1ll1l111_opy_, l1ll1l1ll_opy_