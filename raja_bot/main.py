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

def sleep(n): 
    MonkeyRunner.sleep(n)

def quest_bot():
    while(1):
        log("clicking the quest")
        tap(Elements.da_quest_loc)
        sleep(3)


def devil_awake_bot():
    while (1):
        log("clicking the quest giver")
        tap(Elements.da_quest_giver)
        sleep(2)
        tap(Elements.da_quest_choice_1)
        sleep(10)
        log("clicking the auto click")
        tap(Elements.auto_attack)
        sleep(1) 

        while(1):
            base = device.takeSnapshot()
            log("clicking quest button")
            tap(Elements.da_quest_loc)
            sleep(15)
            result = check_image(base, Elements.card_image)
            if result:
                break
        
        log("waiting for game to finish")
        sleep(15)


def devil_awake_bot():
    while (1):
        log("clicking the quest giver")
        tap(Elements.da_quest_giver)
        sleep(2)
        tap(Elements.da_quest_choice_1)
        sleep(10)
        log("clicking the auto click")
        tap(Elements.auto_attack)
        sleep(1) 

        while(1):
            base = device.takeSnapshot()
            log("clicking quest button")

            if check_image(base, Elements.menu_x):
                tap(Elements.menu_x)

            tap(Elements.da_quest_loc)
            sleep(6)
            result = check_image(base, Elements.card_image)
            if result:
                break
        
        log("waiting for game to finish")
        sleep(15)



def tik_bot():
    while(1):
        base = device.takeSnapshot()
        if check_image(base, Elements.tik_purchase):
            tap(Elements.tik_purchase)
            sleep(1)
        elif check_image(base, Elements.tik_item):
            tap(Elements.tik_item)
        else:
            tap(Elements.da_quest_loc)
            sleep(2)


def ex_bot():
    while(1):
        tap(Elements.ex_loc)
        sleep(180)



if __name__ == "__main__":
    device = MonkeyRunner.waitForConnection()
    #device.touch(0, 0, "DOWN")

    market = False
    buy = False
    selected_game = sys.argv[1]

    if "debug" in sys.argv:
        debug = True

    if selected_game == "da":
        devil_awake_bot()
    elif selected_game == "q":
        quest_bot()
    elif selected_game == "tik":
        tik_bot()
    elif selected_game == "ex":
        ex_bot()

  