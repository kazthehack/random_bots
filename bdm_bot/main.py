import sys

from datetime import datetime
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from bot_types import Elements, GameImage

#####################
# GLOBALS VARIABLES
#####################
f = open("logfile.txt", "w+")
debug = False
device = None


def log(text):
    formatted_text = datetime.now().isoformat() + " " + text
    print(formatted_text)
    f.write(formatted_text + "\n")
    f.flush()


def check_image(base, target, tolerance=0.40, trace=True):
    sub_image = base.getSubImage((target.x, target.y, target.width, target.height))
    target_image = MonkeyRunner.loadImageFromFile("images/" + target.url)
    result = sub_image.sameAs(target_image, tolerance)
    if debug and trace:
        sub_image.writeToFile("debug.png", "png")
        log(target.url + ":" + str(result))
    return result


def check_debug(img, target, tolerance=0.4):
    base = MonkeyRunner.loadImageFromFile("reroll/" + img)
    sub_image = base.getSubImage((target.x, target.y, target.width, target.height))
    target_image = MonkeyRunner.loadImageFromFile("images/" + target.url)
    result = sub_image.sameAs(target_image, tolerance)
    log(str(result))


def tap(element, offset=0, timeout=1, spam=False):
    device.touch(element.x + offset, element.y + offset, MonkeyDevice.DOWN_AND_UP)

    if isinstance(element, GameImage):
        log("tapped: " + element.url)

    if timeout > 0:
        MonkeyRunner.sleep(timeout)


def tap_till_gone(element, offset=0, timeout=1):
    while 1:
        tap(element, offset, timeout)
        base = device.takeSnapshot()
        if check_image(base, element):
            MonkeyRunner.sleep(timeout)
        else:
            break


def tap_wait(
    target,
    result,
    tolerance=0.3,
    offset=0,
    timeout=0,
    extend=0,
    alt=None,
    max_retries=0,
):
    tap(target, offset, timeout)
    if alt:
        tap(alt, offset, timeout)

    retry_count = 0
    MonkeyRunner.sleep(extend)
    while 1:
        base = device.takeSnapshot()
        if check_image(base, result, tolerance):
            return True
        elif (retry_count > max_retries) and max_retries != 0:
            return False
        else:
            retry_count += 1
            MonkeyRunner.sleep(extend)
            tap(target, offset, timeout)
            if alt:
                tap(alt, offset, timeout)


def fishbot():
    count = 0
    while 1:
        base = device.takeSnapshot()
        if debug:
            log(str(count))

        if check_image(base, Elements.fish) or count % 40 == 0:
            tap(Elements.fish, timeout=5)

        if check_image(base, Elements.catch, tolerance=0.55):
            tap(Elements.catch)
            MonkeyRunner.sleep(0.1)
            tap(Elements.pull)
            count = -3

        if check_image(base, Elements.green):
            tap(Elements.pull)
            count = -3

        count += 1


def feed_pets():
    # tap( Elements.pets)
    tap_wait(Elements.pets, Elements.exit_menu, tolerance=0.2, timeout=2, offset=3)
    tap(Elements.pet_loc_1, timeout=2)
    tap(Elements.food, timeout=1)
    tap(Elements.pet_loc_2, timeout=1)
    tap(Elements.food, timeout=1)
    tap(Elements.pet_loc_3, timeout=1)
    tap(Elements.food, timeout=1)
    tap(Elements.exit_menu, timeout=1)


def stone_bs():
    tap_wait(Elements.bs_loc, Elements.bs_exit, timeout=3)
    tap_wait(Elements.bs_lightstone, Elements.bs_ls_auto, timeout=2)
    result = tap_wait(
        Elements.bs_ls_auto, Elements.bs_ls_confirm, timeout=1, max_retries=2
    )
    if result:
        tap(Elements.rare_location)
        tap(Elements.bs_ls_confirm, timeout=10)
    tap(Elements.bs_exit, timeout=2)


def gem_bs():
    tap_wait(Elements.bs_loc, Elements.bs_exit, timeout=3)
    tap_wait(Elements.bs_gems, Elements.bs_gems_auto, timeout=2)
    result = tap_wait(
        Elements.bs_gems_auto, Elements.bs_gems_confirm, timeout=1, max_retries=2
    )

    if result:
        tap(Elements.rare_location)
        tap(Elements.bs_gems_confirm, timeout=10)
    tap(Elements.bs_exit, timeout=2)


def feed_bs():
    tap_wait(Elements.bs_loc, Elements.bs_exit, timeout=3)
    tap(Elements.bs_energy_loc, timeout=2)
    tap(Elements.bs_auto, timeout=2)
    result = tap_wait(Elements.bs_absorb, Elements.bs_confirm, timeout=2, max_retries=2)
    if result:
        tap(Elements.bs_confirm, offset=10, timeout=2)
    tap(Elements.bs_exit, timeout=2)


def repeat_quest():
    LIMIT = 3

    for x in range(LIMIT):
        base = device.takeSnapshot()
        tap(Elements.qs_done, offset=5, timeout=1)
        base = device.takeSnapshot()
        accept = check_image(base, Elements.qs_accept)
        if accept:
            tap_till_gone(Elements.qs_accept, offset=10, timeout=1)
            # tap(Elements.qs_accept,offset=10,timeout=1)
            tap(Elements.qs_dia_loc, timeout=2)
            return
        tap(Elements.qs_done_alt, offset=5, timeout=1)
        base = device.takeSnapshot()
        accept = check_image(base, Elements.qs_accept)
        if accept:
            tap_till_gone(Elements.qs_accept, offset=10, timeout=1)
            # tap(Elements.qs_accept,offset=10,timeout=1)
            tap(Elements.qs_dia_loc, timeout=2)
            return
        tap(Elements.qs_dia_loc, timeout=1)
        base = device.takeSnapshot()
        accept = check_image(base, Elements.qs_accept)
        if accept:
            tap_till_gone(Elements.qs_accept, offset=10, timeout=1)
            # tap(Elements.qs_accept,offset=10,timeout=1)
            tap(Elements.qs_dia_loc, timeout=2)
            return

    check_exit()


def check_exit():
    base = device.takeSnapshot()
    if check_image(base, Elements.exit_modal):
        tap(Elements.exit_modal)


def farmbot(location, minutes, gems, market, buy):
    gametime = 60 * minutes
    start = datetime.utcnow()
    death = False
    loop_count = 0

    while 1:
        now = datetime.utcnow()
        base = device.takeSnapshot()
        seconds = (now - start).seconds

        # Suppress amount of seconds logged
        if debug and (seconds % 10 == 0):
            log(str(seconds))

        # Suppres logs from this since it is annoying
        if check_image(base, Elements.net_dc, trace=False):
            tap(Elements.net_dc)
            log("WARNING: Network Disconnected!")

        if check_image(base, Elements.death_mobs_home, trace=False):
            tap(Elements.death_mobs_home)
            log("WARNING: Death has been encountered")
            MonkeyRunner.sleep(10)
            death = True

        #####
        # Do not add anything  here this already timer level
        #####
        if seconds > gametime or loop_count == 0 or death == True:
            loop_count += 1

            if death is False:
                log("Going Home")
                go_home()

            log("Buying Pots")
            buy_pots(buy)

            # log("Running Gems Bot")
            # result = go_gems(gems)

            # # Check if gems are bought
            # if result:
            #     log("Running BS Gem Bot")
            #     gem_bs()

            log("Running Quest Bot")
            repeat_quest()

            log("Running Feed BS Bot")
            feed_bs()
            MonkeyRunner.sleep(12)

            # Stuff doesn't need to be that often
            # Would save some time
            if (loop_count % 2) == 0:
                log("Running Feed Pet Bot")
                feed_pets()

                log("Running Fuse Lightstone Bot")
                stone_bs()

            log("Running Back Bot")
            go_back(location)

            start = datetime.utcnow()
            death = False


def go_home():
    result = tap_wait(
        Elements.home_loc,
        Elements.home_btn,
        tolerance=0.2,
        timeout=2,
        alt=Elements.outlaw_exit,
        max_retries=5,
    )
    if result is False:
        log("Initial home button failed, checking if stupid modal is there ")
        base = device.takeSnapshot()
        modal_check = check_image(base, Elements.bounty)
        camp_modal_check = check_image(base, Elements.camp)

        if modal_check or camp_modal_check:
            # try to click the empty space
            tap(Elements.anti_bug)
            tap(Elements.anti_bug)
            tap(Elements.anti_bug)
            # BUG: When another modal is displayed by mistake :/
            tap(Elements.anti_bug)
            tap(Elements.anti_bug)
            tap(Elements.anti_bug)
            # Try to rerun the the home command
            sub_result = tap_wait(
                Elements.home_loc,
                Elements.home_btn,
                tolerance=0.2,
                timeout=2,
                alt=Elements.outlaw_exit,
                max_retries=5,
            )

            if sub_result is False:
                log("Bugged on Modal Home")
                exit()

        else:
            log("Bugged on the first call, no modal")
            exit()

    tap(Elements.home_near, timeout=15)

    return


def buy_pots(buy=False):
    result = tap_wait(
        Elements.home_loc,
        Elements.home_btn,
        tolerance=0.2,
        timeout=2,
        alt=Elements.outlaw_exit,
        max_retries=5,
    )
    if result is False:
        log("Initial buy pots failed, checking if stupid modal is there ")
        base = device.takeSnapshot()
        modal_check = check_image(base, Elements.bounty)
        camp_modal_check = check_image(base, Elements.camp)

        if modal_check or camp_modal_check:
            # try to click the empty space
            tap(Elements.anti_bug)
            tap(Elements.anti_bug)
            tap(Elements.anti_bug)
            tap(Elements.anti_bug)
            tap(Elements.anti_bug)
            tap(Elements.anti_bug)
            # Try to rerun the the home command
            sub_result = tap_wait(
                Elements.home_loc,
                Elements.home_btn,
                tolerance=0.2,
                timeout=2,
                alt=Elements.outlaw_exit,
                max_retries=5,
            )

            if sub_result is False:
                log("Modal was closed but still bugged after pots")
                exit

        else:
            log("Modal did not appear and this pots still bugged")
            exit()

    tap(Elements.home_auto_3_loc, timeout=15)

    # Sell all the junk
    tap_wait(Elements.home_pots, Elements.home_sell_junk, offset=10, timeout=2)
    tap(Elements.home_sell_junk, timeout=2)

    if buy:
        # Purchase the Pots
        tap(Elements.home_pots_blue, timeout=1)
        tap(Elements.home_pots_10, timeout=1)
        # tap(Elements.home_pots_10, timeout=1)
        tap(Elements.home_pots_confirm, timeout=1)
        tap(Elements.home_pots_confirm_accept, timeout=1)

    tap(Elements.bs_exit, timeout=2)


# def go_gems(gems_btn):
#     result = tap_wait(
#         Elements.home_loc,
#         Elements.home_btn,
#         tolerance=0.2,
#         timeout=2,
#         alt=Elements.outlaw_exit,
#         max_retries=10,
#     )
#     if result is False:

#         #check_bounty = Chec

#         exit()

#     tap(Elements.home_near, timeout=15)
#     result = tap_wait(
#         Elements.home_loc,
#         Elements.home_btn,
#         tolerance=0.2,
#         timeout=2,
#         alt=Elements.outlaw_exit,
#         max_retries=10,
#     )
#     if result is False:
#         log("BUG BUG BUG #2 ")
#         exit()

#     tap(Elements.home_auto_3_loc, timeout=10)
#     # Sell all the junk
#     tap_wait(gems_btn, Elements.home_sell_junk, timeout=2)
#     tap(Elements.home_sell_junk, timeout=2)

#     # Purchase the Gems
#     # tap_wait( Elements.home_gems, Elements.home_purchase, timeout=2)
#     result = tap_wait(
#         Elements.home_purchase, Elements.home_accept, timeout=2, max_retries=2
#     )
#     if result:
#         tap(Elements.home_accept, timeout=2)
#     tap(Elements.bs_exit, timeout=2)
#     return result


def go_back(location):
    # There is no issues with pathing when going back to the location
    tap_wait(Elements.home_loc, Elements.home_btn, timeout=2)
    tap(location, timeout=10)


def shak_bot():
    count = 0
    while 1:
        tap(Elements.shak_weap, timeout=1)
        count += 1
        log("count: " + str(count))


if __name__ == "__main__":
    device = MonkeyRunner.waitForConnection()
    device.touch(0, 0, "DOWN")

    market = False
    buy = False
    selected_game = sys.argv[1]

    if "debug" in sys.argv:
        debug = True

    if "market" in sys.argv:
        market = True

    if "buy" in sys.argv:
        buy = True

    if selected_game == "fish":
        fishbot()
    elif selected_game == "farm_1":
        farmbot(
            location=Elements.home_auto_1_loc,
            minutes=20,
            gems=Elements.home_gems_2,
            market=market,
            buy=buy,
        )
    elif selected_game == "farm_2":
        farmbot(
            location=Elements.home_auto_2_loc,
            minutes=30,
            gems=Elements.home_gems_2,
            market=market,
            buy=buy,
        )
    elif selected_game == "quest":
        repeat_quest()
    elif selected_game == "home":
        # go_gems(Elements.home_gems_2)
        pass
    elif selected_game == "shak":
        shak_bot()
    elif selected_game == "ls":
        stone_bs()
