from source.util import *
from source.manager.img_manager import LOG_WHEN_TRUE, LOG_ALL, LOG_NONE, LOG_WHEN_FALSE, ImgIcon
from source.manager.button_manager import Button
from source.manager.text_manager import TextTemplate, Text
from source.manager.posi_manager import PosiTemplate, Area
from source.api.utils import *
"""
OLD

DO NOT ADD ANY NEW ASSET HERE. 
USE SOURCE/ASSETS INSTEAD.

"""
# Button&ImgIcon&Area
ButtonUISwitchToTimeMenu = Button(black_offset = 15, print_log=LOG_WHEN_TRUE)
ButtonGeneralExit = Button(print_log=LOG_WHEN_TRUE)
ButtonUICancel = Button(print_log=LOG_WHEN_TRUE)
IconCombatComingOutBySpace = ImgIcon(bbg_posi=[1379,505,1447,568], cap_posi='bbg', threshold=0.8, print_log=LOG_WHEN_TRUE)
IconUIInDomain = ImgIcon(print_log=LOG_WHEN_TRUE)
ButtonGeneralUseOriginResin = ImgIcon(print_log=LOG_WHEN_TRUE)
ButtonGeneralUseCondensedResin = ImgIcon(print_log=LOG_WHEN_TRUE)
IconGeneralFButton = ImgIcon(bbg_posi=[1104,526 , 1128,550 ], cap_posi=[1079,350 ,1162, 751 ],threshold=0.92, print_log=LOG_WHEN_TRUE)
IconBigmapTeleportWaypoint = ImgIcon()
IconBigmapGodStatue = ImgIcon()
IconBigmapDomain = ImgIcon()
IconGeneralMotionSwimming = ImgIcon(bbg_posi=[1808,968,1872,1016], cap_posi='bbg')# 不能删bbg
IconGeneralMotionClimbing = ImgIcon(bbg_posi=[1706,960,1866,1022], cap_posi='bbg')# 不能删bbg
IconGeneralMotionFlying = ImgIcon(bbg_posi=[1706,960,1866,1022], cap_posi='bbg')# 不能删bbg
IconUIEmergencyFood = ImgIcon(print_log=LOG_WHEN_TRUE, threshold=0.97)
IconUIBigmap = ImgIcon(cap_posi=[1300,36,1750, 59 ], print_log=LOG_WHEN_TRUE, threshold=0.97, offset=10)
IconUIEscMenu = ImgIcon(print_log=LOG_WHEN_TRUE, threshold=0.97)
ButtonUISwitchToTimeMenu = Button(print_log=LOG_WHEN_TRUE)
IconUITimeMenuCore = ImgIcon(print_log=LOG_WHEN_TRUE, threshold=0.89)
AreaBigmapChoose = Area()
ButtonBigmapTP = ImgIcon()
ButtonDomainStartChallenge = Button(print_log=LOG_WHEN_TRUE, threshold=0.98)
AreaDomainSwitchChallenge = Area()
ButtonDomainSoloChallenge = Button(print_log=LOG_WHEN_TRUE, threshold=0.98)
character_q_skills = PosiTemplate(img_path=fr"{ASSETS_PATH}/imgs/Windows/Combat/common/AreaCombatQ1.jpg")
character_q_skills.add_posi(img_path=fr"{ASSETS_PATH}/imgs/Windows/Combat/common/AreaCombatQ2.jpg")
character_q_skills.add_posi(img_path=fr"{ASSETS_PATH}/imgs/Windows/Combat/common/AreaCombatQ3.jpg")
character_q_skills.add_posi(img_path=fr"{ASSETS_PATH}/imgs/Windows/Combat/common/AreaCombatQ4.jpg")
ButtonFoodEgg = Button(cap_posi='all', is_bbg = False)
ButtonGeneralConfirm = Button(cap_posi='all', is_bbg = False)
AreaCombatRevivalFoods = Area()
ButtonBigmapSwitchDomainModeOn = Button(threshold=0.97)
ButtonBigmapSwitchDomainModeOff = Button(threshold=0.97)
AreaBigmapSwitchMap = Area()
ButtonBigmapSwitchMap = Button()
IconBigMapScaling = ImgIcon(threshold=0.98, print_log = LOG_ALL, offset=0)
ButtonBigmapCloseMarkTableInTP = Button(threshold=0.999)
AreaCombatBloodBar = Area()
AreaCombatCharacterName1 = Area()
AreaCombatCharacterName2 = Area()
AreaCombatCharacterName3 = Area()
AreaCombatCharacterName4 = Area()
AreaCombatTeamCharactersName = Area()
ButtonUIEnterPartySetup = Button()
CombatButtonGoToFight = Button()
ButtonCombatSwitchTeamLeft = Button(threshold=0)
ButtonCombatSwitchTeamRight = Button(threshold=0)
IconUIPartySetup = ImgIcon(threshold=0.96,print_log=LOG_WHEN_TRUE)
AreaCombatPartySetupCharaName1=Area()
AreaCombatPartySetupCharaName2=Area()
AreaCombatPartySetupCharaName3=Area()
AreaCombatPartySetupCharaName4=Area()
IconBigmapCommission = ImgIcon(is_bbg=False)
AreaBigmapSidebarCommissionName = PosiTemplate()
IconBigmapSidebarIsCommissionExist = ImgIcon(threshold=0.97)
IconCommissionCommissionIcon = ImgIcon()
IconCommissionInCommission = ImgIcon(is_bbg=False)
AreaClaimRewardAvailableReward = PosiTemplate()
AreaDomainLeaveIn = PosiTemplate()
AreaDomainLeyLineDisorder = PosiTemplate()
AreaGeneralInteractiveItemInformation = ImgIcon()
IconGeneralTalkBubble = ImgIcon()

# Text
QTSX = TextTemplate(text={"zh_CN":"七天神像","en_US":"Statues of The Seven"}, cap_area = AreaBigmapChoose.position)
CSMD = TextTemplate(text={"zh_CN":"传送锚点","en_US": "Teleport Waypoint"}, cap_area = AreaBigmapChoose.position)
ASmallStepForHilichurls = TextTemplate(text={"zh_CN":"丘丘人的一小步", "en_US": "A Small Step for"})
IncreasingDanger = TextTemplate(text={"zh_CN":"攀高危险", "en_US": "Increasing Danger"})
Emergency = TextTemplate(text={"zh_CN":"临危受命", "en_US": "Emergency"})
IcyIssues = TextTemplate(text={"zh_CN":"冷冰冰的大麻烦", "en_US": "Icy Issues"})
ForTheHarbingers = TextTemplate(text={"zh_CN":"为了执行官大人", "en_US": "For The Harbingers"})
BigIceColdCrisis = TextTemplate(text={"zh_CN":"冰凉凉的大团危机", "en_US": "Big Ice-Cold Crisis"})
SpreadingEvil = TextTemplate(text={"zh_CN":"邪恶的扩张", "en_US": "Spreading Evil"})
BigPudgyProblem = TextTemplate(text={"zh_CN":"圆滚滚的大团骚乱", "en_US": "Big Pudgy Problem"})
PudgyPyrotechnicians = TextTemplate(text={"zh_CN":"圆滚滚的易爆品", "en_US": "Pudgy Pyrotechnicians"})
MapAreaMD = TextTemplate(text={"zh_CN":"蒙德", "en_US":"Mondstadt"}, cap_area = AreaBigmapSwitchMap.position, match_mode = ACCURATE_MATCHING)
MapAreaLY = TextTemplate(text={"zh_CN":"璃月", "en_US":"Liyue"}, cap_area = AreaBigmapSwitchMap.position, match_mode = ACCURATE_MATCHING)
MapAreaDQ = TextTemplate(text={"zh_CN":"稻妻", "en_US":"Inazuma"}, cap_area = AreaBigmapSwitchMap.position, match_mode = ACCURATE_MATCHING)
MapAreaXM = TextTemplate(text={"zh_CN":"须弥", "en_US":"Sumeru"}, cap_area = AreaBigmapSwitchMap.position, match_mode = ACCURATE_MATCHING)
MapAreaFD = TextTemplate(text={"zh_CN":"枫丹", "en_US":"Fontaine"}, cap_area = AreaBigmapSwitchMap.position, match_mode = ACCURATE_MATCHING)
MapAreaCYJY = TextTemplate(text={"zh_CN":"层岩巨渊", "en_US":"The Chasm"}, cap_area = AreaBigmapSwitchMap.position)
claim_rewards = TextTemplate(text={'zh_CN': '领取奖励',"en_US": "Claim Rewards"})
use_20x2resin = TextTemplate(text={'zh_CN': '使用浓缩树脂',"en_US": "Use Condensed Resin"})
use_20resin = TextTemplate(text={'zh_CN': '使用原粹树脂',"en_US": "Use Original Resin"})
conti_challenge = TextTemplate(text={'zh_CN': '继续挑战',"en_US": "Continue Challenge"})
exit_challenge = TextTemplate(text={'zh_CN': '退出秘境',"en_US": "Leave Domain"})
TextDomainObtain = TextTemplate(text={'zh_CN': '获得', "en_US": "Obtained"})
use_revival_item = TextTemplate(text={'zh_CN': '用道具',"en_US": "revival item"})
revival = Text(zh="复苏", en="Revive")
LEAVING_IN = TextTemplate(text={'zh_CN': '自动退出',"en_US": 'Leaving in'}, cap_area = AreaDomainLeaveIn.position)
LEY_LINE_DISORDER = TextTemplate(text={'zh_CN': '地脉异常',"en_US": "Ley Line Disorder"}, cap_area = AreaDomainLeyLineDisorder.position)

# ImgIcon&Button which based on text
IconCombatCharacterDied = ImgIcon(win_text = use_revival_item.text, threshold=0.98, print_log=LOG_WHEN_TRUE)
ButtonGeneralAllCharacterDied = Button(threshold=0.988, win_text=revival.text, print_log=LOG_WHEN_TRUE)