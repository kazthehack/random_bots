from pkm_types import Elements, GameImage
from main import check_image

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

device = MonkeyRunner.waitForConnection()


def tap(target):
    device.touch(target.x + 30, target.y + 30, "DOWN")
    if isinstance(target, GameImage):
        print("tapping: " + target.url)
    MonkeyRunner.sleep(0.5)


def wait_until_gone(target):
    base = device.takeSnapshot()
    while check_image(base, target,90):
        print("waiting: " + target.url)
        MonkeyRunner.sleep(0.5)


def tap_n_wait(target, result):
    tap(target)
    wait_until_gone(result)

def _check_image(target):
    base = device.takeSnapshot()
    return check_image(base,target,debug=True,tolerance=0.55)


# left - mid - right
# 01 - 03
# 02 - 04

tap(Elements.target_right)
tap_n_wait(Elements.phoebe_03_01, Elements.phoebe_03_02)

# Shadow punch until dead
while 1:
    still_phoebe_01 = _check_image(Elements.phoebe_01_01)
    still_phoebe_02 = _check_image(Elements.phoebe_01_02)
    still_roark_01 = _check_image(Elements.roark_01_01)
    still_roark_02 = _check_image(Elements.roark_01_02)

    if still_phoebe_01:
        tap(Elements.target_right)
        tap(Elements.phoebe_01_01)
        MonkeyRunner.sleep(2)
    elif still_phoebe_02:
        MonkeyRunner.sleep(2)
    elif still_roark_01 or still_roark_02:
        break

buffed = False 
# Assume Roark
while 1:
    still_roark_01 = _check_image(Elements.roark_01_01)
    still_roark_02 = _check_image(Elements.roark_01_02)
    still_olivia_01 = _check_image(Elements.olivia_01_01)
    still_olivia_02 = _check_image(Elements.olivia_01_01)

    if buffed is False:
        tap(Elements.roark_04_01)
        buffed = True 
    elif still_roark_01:
        tap(Elements.roark_02_01)
        buffed=False
    elif still_roark_02:
        MonkeyRunner.sleep(2)
    elif still_olivia_01 or still_olivia_02:
        break

# Assume Olivia
hardened = False
while 1:
    still_olivia_01 = _check_image(Elements.olivia_01_01)
    still_olivia_02 = _check_image(Elements.olivia_01_01)
    olivia_sync = _check_image(Elements.olivia_sync_01)

    if olivia_sync:
        tap_n_wait
    elif hardened is False:
        tap_n_wait(Elements.olivia_04_01, Elements.olivia_04_02)
        hardened = True
    elif still_olivia_01:
        tap_n_wait(Elements.olivia_02_01, Elements.olivia_02_02)
    elif still_olivia_02:
        MonkeyRunner.sleep(0.5)
