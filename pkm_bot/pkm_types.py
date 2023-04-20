class Location:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class GameImage:
    def __init__(self, url, height, width, x, y):
        self._url = url
        self._height = height
        self._width = width
        self._location = Location(x, y)

    @property
    def url(self):
        return self._url

    @property
    def x(self):
        return self._location.x

    @property
    def y(self):
        return self._location.y

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height


class Elements:
    current = "temp.png"
    # Game Input
    go = GameImage("go_btn.png", 144, 434, 318, 1751)
    ok = GameImage("ok_btn.png", 143, 414, 334, 1744)
    ok2 = GameImage("ok_btn2.png", 140, 414, 335, 1748)
    battle_again = GameImage("battle_again.png", 145, 425, 567, 1747)
    explore = GameImage("explore_btn.png", 166, 190, 448, 1664)
    coop_quick = GameImage("coop_quick_btn.png", 421, 429, 88, 775)
    return_btn = GameImage("return_btn.png", 137, 125, 0, 1759)
    confirm = GameImage("confirm_btn.png", 146, 434, 563, 1216)

    solo_tab = GameImage("single_btn.png", 114, 472, 55, 151)
    coop_tab = GameImage("coop_btn.png", 103, 476, 549, 154)
    solo_train_btn = GameImage("solo_train_btn.png", 181, 988, 47, 1083)
    solo_level_btn = GameImage("solo_level.png", 141, 983, 47, 301)
    solo_strike_btn = GameImage("solo_strike_btn.png", 244, 994, 43, 694)
    solo_support_btn = GameImage("solo_support_btn.png", 237, 990, 43, 1336)
    solo_tech_btn = GameImage("solo_tech_btn.png", 245, 994, 42, 1014)
    coop_mission_btn = GameImage("coop_mission_btn.png", 174, 984, 56, 354)
    coop_event_btn = GameImage("coop_event_btn.png", 181, 975, 62, 597)
    coop_event = GameImage("coop_event.png", 210, 880, 91, 393)
    solo_event_btn = GameImage("solo_event_btn.png", 181, 975, 62, 597)
    solo_event = GameImage("solo_event.png", 210, 880, 91, 393)

    coop_train_btn = GameImage("coop_train_btn.png", 185, 992, 51, 839)
    coop_train_03 = GameImage("coop_train_03.png", 235, 995, 42, 1021)
    coop_train_03_02 = GameImage("coop_train_03_02.png", 218, 978, 51, 414)
    coop_train_03_03 = GameImage("coop_train_03_03.png", 211, 971, 50, 747)
    coop_train_06 = GameImage("coop_train_06.png", 244, 978, 53, 525)
    coop_train_06_02 = GameImage("coop_train_06_02.png", 218, 978, 51, 414)
    coop_train_06_03 = GameImage("coop_train_06_03.png", 211, 971, 50, 747)
    coop_train_09 = GameImage("coop_train_09.png", 235, 995, 42, 1171)
    coop_train_09_02 = GameImage("coop_train_09_02.png", 218, 978, 51, 414)
    coop_train_09_03 = GameImage("coop_train_09_03.png", 211, 971, 50, 747)
    coop_back = GameImage("coop_back.png", 140,347,131,1722)

    coop_16 = GameImage("coop_mission_16.png", 240, 988, 40, 852)
    coop_14 = GameImage("coop_mission_14.png", 213, 985, 44, 1497)
    coop_12 = GameImage("coop_mission_12.png", 238, 989, 50, 819)
    coop_01 = GameImage("coop_mission_01.png", 240, 985, 42, 1454)

    # Result_Page
    level_up = GameImage("levelup_result.png", 82, 154, 772, 681)
    xp_result = GameImage("xp_result.png", 96, 495, 29, 103)

    # Stage Selection
    solo_level_02 = GameImage("levelupcourse_02.png", 222, 979, 50, 739)
    solo_level_03 = GameImage("levelupcourse_03.png", 222, 979, 51, 412)
    solo_level_01 = GameImage("levelupcourse_01.png", 222, 979, 50, 1066)

    solo_support_02 = GameImage("supportcourse_02.png", 222, 979, 50, 739)
    solo_support_03 = GameImage("supportcourse_03.png", 222, 979, 51, 412)

    solo_strike_02 = GameImage("strikecourse_02.png", 222, 979, 50, 739)
    solo_strike_03 = GameImage("strikecourse_03.png", 222, 979, 51, 412)

    solo_tech_02 = GameImage("techcourse_02.png", 222, 979, 50, 739)
    solo_tech_03 = GameImage("techcourse_03.png", 222, 979, 51, 412)

    solo_event_01 = GameImage("solo_event_01.png", 221, 981, 48, 1158)

    coop_14_03 = GameImage("coop_14_03.png", 218, 979, 46, 249)
    coop_14_02 = GameImage("coop_14_02.png", 222, 979, 45, 576)
    coop_16_03 = GameImage("coop_16_03.png", 218, 979, 46, 249)
    coop_16_02 = GameImage("coop_16_02.png", 222, 979, 45, 576)
    coop_12_03 = GameImage("coop_12_03.png", 218, 979, 46, 249)
    coop_01_03 = GameImage("coop_01_03.png", 218, 979, 46, 249)
    coop_01_02 = GameImage("coop_01_02.png", 222, 979, 45, 576)

    coop_event_02 = GameImage("coop_event_02.png", 218, 979, 58, 374)
    coop_event_01 = GameImage("coop_event_01.png", 222, 979, 49, 690)
    coop_event_legendary_02 = GameImage(
        "coop_event_legendary_02.png", 218, 979, 47, 971
    )
    coop_event_legendary_01 = GameImage(
        "coop_event_legendary_01.png", 218, 979, 47, 1291
    )

    rewards_bar = GameImage("rewards_bar.png", 67, 976, 58, 237)

    target_left = Location(156, 416)
    target_mid = Location(508, 416)
    target_right = Location(832, 416)

    matching_room_01 = GameImage("matching_room_01.png", 88, 628, 0, 0)
    matching_room_02 = GameImage("matching_room_02.png", 88, 628, 0, 0)
    not_enough_npc = GameImage("reset_dialog.png", 969, 983, 50, 475)
    no_btn = GameImage("no_btn.png", 152, 432, 98, 1213)
    yes_btn = GameImage("yes_btn.png", 154, 436, 556, 1213)

    auto_on = GameImage("auto_on.png", 62, 145, 914, 21)
    auto_off = GameImage("auto_off.png", 62, 145, 914, 21)

    dc_dialog = GameImage("dc_dialog.png", 963, 982, 49, 479)
    dc_quit = GameImage("dc_quit.png", 156, 429, 98, 1211)

    # left - mid - right
    # 01 - 03
    # 02 - 04

    # Olivia
    olivia_01_01 = GameImage("olivia_01_01.png", 173, 169, 292, 1403)
    olivia_02_01 = GameImage("olivia_02_01.png", 176, 174, 290, 1594)
    olivia_03_01 = GameImage("olivia_03_01.png", 175, 179, 619, 1401)
    olivia_04_01 = GameImage("olivia_04_01.png", 181, 180, 617, 1587)
    olivia_01_02 = GameImage("olivia_01_02.png", 173, 169, 292, 1403)
    olivia_02_02 = GameImage("olivia_02_02.png", 176, 174, 290, 1594)
    olivia_03_02 = GameImage("olivia_03_02.png", 175, 179, 619, 1401)
    olivia_04_02 = GameImage("olivia_04_02.png", 181, 180, 617, 1587)
    olivia_sync_01 = GameImage("olivia_sync_01.png", 125, 91, 493, 1502)
    olivia_sync_02 = GameImage("olivia_sync_02.png", 125, 91, 493, 1502)

    # Phoebe
    phoebe_01_01 = GameImage("phoebe_01_01.png", 173, 169, 292, 1403)
    phoebe_02_01 = GameImage("phoebe_02_01.png", 176, 174, 290, 1594)
    phoebe_03_01 = GameImage("phoebe_03_01.png", 175, 179, 619, 1401)
    phoebe_04_01 = GameImage("phoebe_04_01.png", 181, 180, 617, 1587)
    phoebe_01_02 = GameImage("phoebe_01_02.png", 173, 169, 292, 1403)
    phoebe_02_02 = GameImage("phoebe_02_02.png", 176, 174, 290, 1594)
    phoebe_03_02 = GameImage("phoebe_03_02.png", 175, 179, 619, 1401)
    phoebe_04_02 = GameImage("phoebe_04_02.png", 181, 180, 617, 1587)

    # Roark
    roark_01_01 = GameImage("roark_01_01.png", 173, 169, 292, 1403)
    roark_02_01 = GameImage("roark_02_01.png", 176, 174, 290, 1594)
    roark_03_01 = GameImage("roark_03_01.png", 175, 179, 619, 1401)
    roark_04_01 = GameImage("roark_04_01.png", 181, 180, 617, 1587)
    roark_01_02 = GameImage("roark_01_02.png", 173, 169, 292, 1403)
    roark_02_02 = GameImage("roark_02_02.png", 176, 174, 290, 1594)
    roark_03_02 = GameImage("roark_03_02.png", 175, 179, 619, 1401)
    roark_04_02 = GameImage("roark_04_02.png", 181, 180, 617, 1587)
