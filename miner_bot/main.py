import sys
import datetime

from datetime import datetime, time
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

def craft_materials():
    tap(Elements.craft_btn)
    sleep(1)
    tap(Elements.m1)
    sleep(0.5)
    tap(Elements.m2)
    sleep(0.5)
    tap(Elements.m3)
    sleep(0.5)
    tap(Elements.m4)
    sleep(0.5)
    tap(Elements.m5)
    sleep(0.5)
    tap(Elements.m6)
    sleep(0.5)
    tap(Elements.exit_btn)
    sleep(1)

def mine_bot(craft_ores=False):
    start_dt = datetime.utcnow()
    
    while(1):
        cur_dt = datetime.utcnow()
        diff = cur_dt - start_dt

        if diff.seconds > 300 and craft_ores: # 5 Mins
            craft_materials()
            start_dt = cur_dt

        sleep(0.1)
        tap(Elements.box_loc,timeout=0)
        tap(Elements.center_loc,timeout=0)
        tap(Elements.exit_window,timeout=0)

if __name__ == "__main__":
    device = MonkeyRunner.waitForConnection()
    #device.touch(0, 0, "DOWN")

    market = False
    buy = False
    selected_game = sys.argv[1]

    if "debug" in sys.argv:
        debug = True

    if selected_game == "mine":
        mine_bot(True)
    elif selected_game == "mine_only":
        mine_bot()

  