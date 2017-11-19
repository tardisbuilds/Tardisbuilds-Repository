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
import json
import tardis
def getURL(url):
    response = l1l1l1l1_opy_(url)
    stream   = url.split(l1111l_opy_ (u"ࠫ࠿࠭ࢯ"), 1)[-1].lower()
    try:
        result = response[l1111l_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬࢰ")]
        l1lll111_opy_  = result[l1111l_opy_ (u"࠭ࡦࡪ࡮ࡨࡷࠬࢱ")]
    except Exception as e:
        l1l1l1ll_opy_(e)
        return None
    for file in l1lll111_opy_:
        l1l1llll_opy_ = file[l1111l_opy_ (u"ࠧ࡭ࡣࡥࡩࡱ࠭ࢲ")]
        if stream == l1l1llll_opy_.lower():
            return file[l1111l_opy_ (u"ࠨࡨ࡬ࡰࡪ࠭ࢳ")]
    return None
def l1l1l1l1_opy_(url):
    if url.startswith(l1111l_opy_ (u"ࠩࡌࡔࡑࡇ࡙࠻ࠩࢴ")):
        l1ll1ll1_opy_ = (l1111l_opy_ (u"ࠪࡿࠧࡰࡳࡰࡰࡵࡴࡨࠨ࠺ࠣ࠴࠱࠴ࠧ࠲ࠠࠣ࡯ࡨࡸ࡭ࡵࡤࠣ࠼ࠥࡊ࡮ࡲࡥࡴ࠰ࡊࡩࡹࡊࡩࡳࡧࡦࡸࡴࡸࡹࠣ࠮ࠣࠦࡵࡧࡲࡢ࡯ࡶࠦ࠿ࢁࠢࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠥ࠾ࠧࡶ࡬ࡶࡩ࡬ࡲ࠿࠵࠯ࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡢࡣࡥ࡬ࡴࡱࡧࡹࡦࡴ࠲ࡃࡺࡸ࡬࠾ࡷࡵࡰࠫࡳ࡯ࡥࡧࡀ࠶ࠫࡴࡡ࡮ࡧࡀࡐ࡮ࡼࡥࠧ࡫ࡦࡳࡳ࡯࡭ࡢࡩࡨࡁࠫࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࡀࠪࡎࡖࡉࡅ࠿ࠥࢁ࠱ࠦࠢࡪࡦࠥ࠾ࠥ࠷ࡽࠨࢵ"))
    if url.startswith(l1111l_opy_ (u"ࠫࡎࡖࡌࡂ࡛࠵࠾ࠬࢶ")):
        l1ll1ll1_opy_ = (l1111l_opy_ (u"ࠬࢁࠢ࡫ࡵࡲࡲࡷࡶࡣࠣ࠼ࠥ࠶࠳࠶ࠢ࠭ࠢࠥࡱࡪࡺࡨࡰࡦࠥ࠾ࠧࡌࡩ࡭ࡧࡶ࠲ࡌ࡫ࡴࡅ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠥ࠰ࠥࠨࡰࡢࡴࡤࡱࡸࠨ࠺ࡼࠤࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧࡀࠢࡱ࡮ࡸ࡫࡮ࡴ࠺࠰࠱ࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯࡫ࡳࡰࡦࡿࡥࡳࡹࡺࡻ࠴ࡅࡵࡳ࡮ࡀࡹࡷࡲࠦ࡮ࡱࡧࡩࡂ࠷࠰࠲ࠨࡱࡥࡲ࡫࠽ࡘࡣࡷࡧ࡭࠱ࡌࡪࡸࡨࠪ࡮ࡩ࡯࡯࡫ࡰࡥ࡬࡫࠽ࠧࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳࡃࠦࡴࡷࡥࡸ࡮ࡺ࡬ࡦࡵࡢࡹࡷࡲ࠽ࠧ࡮ࡲ࡫࡬࡫ࡤࡠ࡫ࡱࡁࡋࡧ࡬ࡴࡧࠥࢁ࠱ࠦࠢࡪࡦࠥ࠾ࠥ࠷ࡽࠨࢷ"))
    if url.startswith(l1111l_opy_ (u"࠭ࡉࡑࡎࡄ࡝ࡗࡀࠧࢸ")):
        l1ll1ll1_opy_ = (l1111l_opy_ (u"ࠧࡼࠤ࡭ࡷࡴࡴࡲࡱࡥࠥ࠾ࠧ࠸࠮࠱ࠤ࠯ࠤࠧࡳࡥࡵࡪࡲࡨࠧࡀࠢࡇ࡫࡯ࡩࡸ࠴ࡇࡦࡶࡇ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧ࠲ࠠࠣࡲࡤࡶࡦࡳࡳࠣ࠼ࡾࠦࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠻ࠤࡳࡰࡺ࡭ࡩ࡯࠼࠲࠳ࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱࡭ࡵࡲࡡࡺࡧࡵࡻࡼࡽ࠯ࡀࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳࠬࡩࡤࡱࡱ࡭ࡲࡧࡧࡦ࠿ࡇࡩ࡫ࡧࡵ࡭ࡶࡉࡳࡱࡪࡥࡳ࠰ࡳࡲ࡬ࠬ࡬ࡰࡩࡪࡩࡩࡥࡩ࡯࠿ࡉࡥࡱࡹࡥࠧ࡯ࡲࡨࡪࡃ࠱࠲࠵ࠩࡲࡦࡳࡥ࠾ࡎ࡬ࡷࡹ࡫࡮ࠦ࠴࠳ࡐ࡮ࡼࡥࠧࡵࡸࡦࡹ࡯ࡴ࡭ࡧࡶࡣࡺࡸ࡬ࠧࡷࡵࡰࡂࡻࡲ࡭ࠤࢀ࠰ࠥࠨࡩࡥࠤ࠽ࠤ࠶ࢃࠧࢹ"))
    if url.startswith(l1111l_opy_ (u"ࠨࡋࡓࡐࡆ࡟ࡉࡕࡘ࠽ࠫࢺ")):
        l1ll1ll1_opy_ = (l1111l_opy_ (u"ࠩࡾࠦ࡯ࡹ࡯࡯ࡴࡳࡧࠧࡀࠢ࠳࠰࠳ࠦ࠱ࠦࠢ࡮ࡧࡷ࡬ࡴࡪࠢ࠻ࠤࡉ࡭ࡱ࡫ࡳ࠯ࡉࡨࡸࡉ࡯ࡲࡦࡥࡷࡳࡷࡿࠢ࠭ࠢࠥࡴࡦࡸࡡ࡮ࡵࠥ࠾ࢀࠨࡤࡪࡴࡨࡧࡹࡵࡲࡺࠤ࠽ࠦࡵࡲࡵࡨ࡫ࡱ࠾࠴࠵ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳࡯ࡴࡷࠤࢀ࠰ࠥࠨࡩࡥࠤ࠽ࠤ࠶ࢃࠧࢻ"))
    if url.startswith(l1111l_opy_ (u"ࠪࡍࡕࡒࡁ࡚࠴࠽ࠫࢼ")):
        l1ll1ll1_opy_ = (l1111l_opy_ (u"ࠫࢀࠨࡪࡴࡱࡱࡶࡵࡩࠢ࠻ࠤ࠵࠲࠵ࠨࠬࠡࠤࡰࡩࡹ࡮࡯ࡥࠤ࠽ࠦࡋ࡯࡬ࡦࡵ࠱ࡋࡪࡺࡄࡪࡴࡨࡧࡹࡵࡲࡺࠤ࠯ࠤࠧࡶࡡࡳࡣࡰࡷࠧࡀࡻࠣࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠦ࠿ࠨࡰ࡭ࡷࡪ࡭ࡳࡀ࠯࠰ࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡪࡲ࡯ࡥࡾ࡫ࡲࡸࡹࡺ࠳ࡄࡻࡲ࡭࠿ࡸࡶࡱࠬ࡭ࡰࡦࡨࡁ࠶࠶࠱ࠧࡰࡤࡱࡪࡃࡗࡢࡶࡦ࡬࠰ࡒࡩࡷࡧࠩ࡭ࡨࡵ࡮ࡪ࡯ࡤ࡫ࡪࡃࠦࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࡂࠬࡳࡶࡤࡷ࡭ࡹࡲࡥࡴࡡࡸࡶࡱࡃࠦ࡭ࡱࡪ࡫ࡪࡪ࡟ࡪࡰࡀࡊࡦࡲࡳࡦࠤࢀ࠰ࠥࠨࡩࡥࠤ࠽ࠤ࠶ࢃࠧࢽ"))
    try:
        tardis.ShowBusy()
        response = xbmc.executeJSONRPC(l1ll1ll1_opy_)
        tardis.CloseBusy()
        content = json.loads(response)
        return content
    except Exception as e:
        l1l1l1ll_opy_(e)
        return {l1111l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠫࢾ") : l1111l_opy_ (u"࠭ࡐ࡭ࡷࡪ࡭ࡳࠦࡅࡳࡴࡲࡶࠬࢿ")}
def l1l1l1ll_opy_(e):
    l1ll1111_opy_ = l1111l_opy_ (u"ࠧࡔࡱࡵࡶࡾ࠲ࠠࡢࡰࠣࡩࡷࡸ࡯ࡳࠢࡲࡧࡨࡻࡲࡦࡦ࠽ࠤࡏ࡙ࡏࡏࠢࡈࡶࡷࡵࡲ࠻ࠢࠨࡷࠬࣀ")  %e
    l1l1ll11_opy_ = l1111l_opy_ (u"ࠨࡒ࡯ࡩࡦࡹࡥࠡࡴࡨ࠱ࡱ࡯࡮࡬ࠢࡷ࡬࡮ࡹࠠࡤࡪࡤࡲࡳ࡫࡬ࠡࡣࡱࡨࠥࡺࡲࡺࠢࡤ࡫ࡦ࡯࡮࠯ࠩࣁ")
    l1ll11l1_opy_ = l1111l_opy_ (u"ࠩࡘࡷࡪࡀࠠࡄࡱࡱࡸࡪࡾࡴࠡࡏࡨࡲࡺࠦ࠽࠿ࠢࡕࡩࡲࡵࡶࡦࠢࡖࡸࡷ࡫ࡡ࡮ࠩࣂ")
    tardis.log(e)
    tardis.DialogOK(l1ll1111_opy_, l1l1ll11_opy_, l1ll11l1_opy_)