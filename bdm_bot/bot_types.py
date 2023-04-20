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
    # Fish Bot
    fish = GameImage("fish_btn.png", 94, 117, 1685, 857)
    catch = GameImage("catch_btn.png", 37, 18, 1735, 885)
    pull = GameImage("pull_btn.png", 16, 19, 1737, 873)
    green = GameImage("green_btn.png", 56, 60, 1220, 400)

    rare_location = Location(950, 661)

    # Farm Bot
    # Old confirm button
    # confirm = GameImage("confirm_btn_3.png", 90, 236, 845, 824)
    confirm = GameImage("confirm_btn.png", 22, 101, 920, 852)
    sword = GameImage("sword.png", 155, 16, 960, 455)
    black_spirit_on = GameImage("black_spirit_on.png", 106, 337, 1464, 923)

    pets = Location(243, 518)
    exit_menu = GameImage("exit_menu.png", 46, 39, 1818, 28)
    food = GameImage("pet_food.png", 42, 72, 608, 973)

    pet_loc_1 = Location(1434, 288)
    pet_loc_2 = Location(1434, 472)
    pet_loc_3 = Location(1434, 659)

    # Black Spirit Bot
    farm_state = GameImage("farm_state.png", 58, 293, 1559, 801)
    bs_loc = Location(1246, 969)
    bs_energy_loc = Location(796, 950)
    bs_auto = GameImage("auto_select.png", 121, 592, 1289, 913)
    bs_absorb = GameImage("absorb_energy.png", 106, 222, 915, 939)
    bs_confirm = GameImage("bs_confirm.png", 103, 255, 968, 731)
    bs_exit = GameImage("bs_exit.png", 48, 42, 1817, 27)

    bs_lightstone = Location(240, 866)
    bs_gems = Location(1705, 760)

    bs_ls_auto = GameImage("ls_auto.png", 104, 275, 1290, 937)
    bs_ls_confirm = GameImage("ls_confirm.png", 103, 252, 968, 780)

    bs_gems_auto = GameImage("gems_auto.png", 104, 275, 1290, 937)
    bs_gems_confirm = GameImage("gems_confirm.png", 103, 252, 968, 780)

    # Quest Bot
    qs_done = GameImage("quest_done.png", 72, 60, 1472, 379)
    # qs_done = GameImage("quest_done_t.png", 72, 60, 1472, 359)
    qs_done_alt = GameImage("quest_done_alt.png", 72, 60, 1472, 455)
    # qs_done_alt = GameImage("quest_done_alt.png", 72, 60, 1472, 435)
    qs_dia_loc = Location(990, 990)
    qs_shrine = GameImage("quest_shrine.png", 612, 230, 205, 468)
    qs_bs = GameImage("quest_bs.png", 361, 126, 262, 470)
    qs_accept = GameImage("quest_accept.png", 105, 252, 969, 807)

    # Home Bot
    home_loc = Location(477, 265)
    home_near = Location(900, 370)
    home_btn = GameImage("home_btn.png", 102, 216, 1250, 640)
    home_auto_1_loc = Location(1350, 530)
    home_auto_2_loc = Location(1350, 660)
    home_auto_3_loc = Location(1350, 790)
    home_pots = GameImage("home_pots.png", 50, 34, 1592, 660)
    home_gems = GameImage("home_gems.png", 50, 34, 1592, 660)
    home_gems_2 = GameImage("home_gems_2.png", 50, 34, 1765, 660)
    home_purchase = GameImage("purchase_all.png", 101, 261, 51, 931)
    home_accept = GameImage("home_accept.png", 105, 252, 969, 837)

    home_pots_blue = Location(320, 714)
    home_pots_10 = Location(1118, 469)
    home_pots_confirm = Location(1086, 913)
    home_pots_confirm_accept = Location(1068, 877)

    home_sell_junk = GameImage("home_sell_junk.png", 103, 282, 1592, 931)

    # Death
    death_sword = GameImage("death_sword.png", 155, 16, 960, 455)
    death_home = GameImage("death_home.png", 100, 280, 1017, 714)
    death_outlaw = Location(683, 55)
    death_deactivate = GameImage("death_deactivate.png", 91, 248, 528, 764)
    outlaw_exit = Location(1388, 249)
    death_mobs_home = GameImage("death_mobs_home.png", 93, 282, 1014, 609)

    # Market
    mkt_hamburger = Location(1856, 56)
    mkt_market_btn = GameImage("market_btn.png", 50, 58, 1498, 435)
    mkt_consumables_btn = Location(200, 980)
    mkt_others = Location(570, 820)
    mkt_black_pearls = Location(1010, 1010)
    mkt_refresh_loc = Location(1748, 287)
    mkt_bid_loc_1 = Location(1740, 502)
    mkt_bid_loc_2 = Location(1740, 644)
    mkt_bid_loc_3 = Location(1740, 784)

    mkt_max = Location(1120, 780)
    mkt_calc_confirm = Location(1100, 920)

    black_pearls = GameImage("black_pearls.png", 88, 100, 790, 972)
    color_palette = GameImage("color_palette.png", 70, 105, 787, 449)
    confirm_bid_btn = GameImage("confirm_bid_btn.png", 104, 262, 963, 733)
    flavor_text = GameImage("flavor_text.png", 39, 344, 900, 251)

    auto_attack = Location(692, 984)
    flip_btn = GameImage("flip_btn.png", 50, 53, 1772, 943)
    flip_2_btn = GameImage("flip_2_btn.png", 50, 53, 1772, 943)
    exit_modal = GameImage("exit_modal.png", 38, 29, 1524, 139)

    net_dc = GameImage("net_dc.png", 105, 248, 837, 726)
    horse = GameImage("horse.png", 65, 79, 25, 514)

    quest_loc_sm = Location(1859, 315)
    quest_loc_sm_alt = Location(1859, 405)

    shak_weap = Location(1366, 828)

    # Bounty Bug
    bounty = GameImage("bounty_modal.png", 588, 958, 481, 237)
    camp = GameImage("camp_modal.png", 588, 958, 481, 237)
    anti_bug = Location(47, 856)
