import os
import sys
import signal
import subprocess

from datetime import datetime
from os.path import splitext, basename
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

from pkm_types import Elements, GameImage


def log(text):
    print(datetime.now().isoformat() + " " + text)


def check_image(base, target, tolerance=0.75, debug=False):
    sub_image = base.getSubImage((target.x, target.y, target.width, target.height))
    target_image = MonkeyRunner.loadImageFromFile("images/" + target.url)
    result = sub_image.sameAs(target_image, tolerance)
    if debug:
        sub_image.writeToFile("debug.png", "png")
        print(target.url + ":" + str(result))
    return result


class PokemonMastersBot:
    def __init__(self, device):
        self._device = device

    def tap(self, element, offset=0, timeout=2, spam=False):
        self._device.touch(element.x + offset, element.y + offset, "DOWN")
        if spam:
            self._device.touch(element.x + offset, element.y + offset, "DOWN")
            MonkeyRunner.sleep(0.1)
            self._device.touch(element.x + offset, element.y + offset, "DOWN")
            MonkeyRunner.sleep(0.1)
            self._device.touch(element.x + offset, element.y + offset, "DOWN")
            MonkeyRunner.sleep(0.1)
            self._device.touch(element.x + offset, element.y + offset, "DOWN")
            MonkeyRunner.sleep(0.1)
            self._device.touch(element.x + offset, element.y + offset, "DOWN")

        if isinstance(element, GameImage):
            print("tapped: " + element.url)

        if timeout > 0:
            MonkeyRunner.sleep(timeout)

    def tap_loc(self, loc, offset=0):
        self._device.touch(loc[0] + offset, loc[1] + offset)

    def wait(self, target):
        while 1:
            base = self._device.takeSnapshot()
            result = check_image(base, target)
            if result:
                break
            else:
                MonkeyRunner.sleep(0.5)

    def wait_until(self, target):
        tapped = False
        tap_limit = 10
        tap_count = 0
        while 1:
            base = self._device.takeSnapshot()
            result = check_image(base, target)

            try:
                if tapped and not result:
                    log("tap ok!!")
                    break
                elif tapped and result:
                    log("tap reset")
                    # tap is not successful.
                    # continue the loop
                    tapped = False
                elif result:
                    log("tap!")
                    self.tap(target, 10)
                    tapped = True
                else:
                    log("Waiting for " + target.url + "...")
                    if tap_count == tap_limit:
                        break
                    else:
                        tap_count = tap_count + 1

                    MonkeyRunner.sleep(1)
            except:
                log("Tap Exception Encountered")
                return False

    def tap_and_wait(self, base, result, offset=0, timeout=0):
        while 1:
            self.tap(base, offset=offset, timeout=timeout)
            dc_dialog = self._check_image(Elements.dc_dialog)
            current = self._device.takeSnapshot()
            if dc_dialog:
                return
            elif check_image(current, result):
                break
            else:
                log("Waiting for tap (" + base.url + ")to succeed...")
                MonkeyRunner.sleep(0.25)

    def wait_until_gone(self, target):
        base = device.takeSnapshot()
        while check_image(base, target, 90):
            print("waiting: " + target.url)
            MonkeyRunner.sleep(0.5)

    def tap_n_wait(self, target, result):
        self.tap(target, offset=30, timeout=0.5)
        self.wait_until_gone(result)

    def _check_image(self, target, tolerance=0.65):
        base = device.takeSnapshot()
        return check_image(base, target, debug=False, tolerance=tolerance)

    def play_game(self, selected_game):
        TIMEOUT = 500
        time = 0
        coop_done = False
        ok_count = 0
        win = False
        log("Game Start!!!")
        start = datetime.utcnow()
        while 1:
            base = self._device.takeSnapshot()

            ok = check_image(base, Elements.ok)
            ok2 = check_image(base, Elements.ok2)
            confirm = check_image(base, Elements.confirm)
            battle_again = check_image(base, Elements.battle_again, tolerance=0.85)
            rewards_bar = check_image(base, Elements.rewards_bar)
            coop_back = check_image(base, Elements.coop_back)

            if confirm:
                self.tap(Elements.confirm)

            banner = check_image(base, selected_game)

            if battle_again:
                # Solo
                log("Battle Again! You win!")
                game_time = (datetime.utcnow() - start).seconds
                log("Game Time:" + "[" + str(game_time) + "]")
                return True, game_time
            elif rewards_bar:
                ok_count += 1
                # if ok_count == 2:
                #     self._capture_screen()
                win = True
            elif coop_back:
                self.tap(Elements.coop_back)
                game_time = (datetime.utcnow() - start).seconds
                return False, game_time
            elif banner and win is False:
                log("Banner Button, You lost")
                game_time = (datetime.utcnow() - start).seconds
                log("Game Time:" + "[" + str(game_time) + "]")
                return win, game_time
            elif banner and win is True:
                log("Battle Won! You win!")
                game_time = (datetime.utcnow() - start).seconds
                log("Game Time:" + "[" + str(game_time) + "]")
                return win, game_time
            

            # if time < 30:
            #     self.tap(Elements.target_right, offset=30, timeout=0.1)
            # elif time > 30 and time < 80:
            #     self.tap(Elements.target_left, offset=30, timeout=0.1)

            if ok:
                self.tap(Elements.ok)
            elif ok2:
                self.tap(Elements.ok2)
            elif selected_game == Elements.coop_train_06_02 and coop_done == False:
                # Auto AI Goes Here
                self.olivia_vh()
                coop_done = True
            else:
                # Place Holder
                self._device.touch(550, 1900, "DOWN")
                MonkeyRunner.sleep(1)

                if time == TIMEOUT:
                    self.tap(Elements.return_btn)
                    return False
                time = time + 1

    def prep_game(self, init_game, mode):

        if "coop" in mode.url:
            # Game is in coop mode
            if init_game:
                self.tap_and_wait(Elements.explore, Elements.solo_tab)
                self.wait_until(Elements.coop_tab)
                # browse until where
                mission_string = basename(mode.url).split("_")
                if mission_string[1] == "event":
                    self.wait_until(Elements.coop_event_btn)
                    self.wait_until(Elements.coop_event)
                elif mission_string[1] == "train":
                    self.wait_until(Elements.coop_train_btn)
                    screen = int(mission_string[2])
                    if screen > 4:
                        log("Dragging right now!")
                        self._device.drag((500, 1700), (500, 200), 0.5, 20)

                    mission_btn = getattr(Elements, "coop_train_" + mission_string[2])
                    self.wait_until(mission_btn)
                else:
                    self.wait_until(Elements.coop_mission_btn)
                    screen = int(mission_string[1])
                    log(str(screen))
                    if screen < 14:
                        # do the drag
                        log("Dragging right now!")
                        self._device.drag((500, 1700), (500, 200), 0.5, 20)

                    mission_btn = getattr(Elements, "coop_" + mission_string[1])
                    self.wait_until(mission_btn)
                self.wait_until(mode)
                self.wait_until(Elements.coop_quick)
        else:
            # Game is in singular player mode
            if init_game:
                self.tap_and_wait(Elements.explore, Elements.solo_tab)
                    
                mission_string = basename(mode.url).split("_")
                if mission_string[1] == "event":
                    self.wait_until(Elements.solo_event_btn)
                    self.wait_until(Elements.solo_event)
                else:
                    self.wait_until(Elements.solo_train_btn)
                    log("Dragging right now!")
                    self._device.drag((500, 1700), (500, 200), 0.5, 20)

                    # add checking
                    if "level" in mode.url:
                        self.wait_until(Elements.solo_level_btn)
                    elif "tech" in mode.url:
                        self.wait_until(Elements.solo_tech_btn)
                    elif "support" in mode.url:
                        self.wait_until(Elements.solo_support_btn)
                    elif "strike" in mode.url:
                        self.wait_until(Elements.solo_strike_btn)
            self.wait_until(mode)

    def _capture_screen(self):
        result = self._device.takeSnapshot()

        # Writes the screenshot to a file
        filename = None
        ROOTDIR = "screens/"
        for i in range(1000):
            if not os.path.isfile(ROOTDIR + str(i) + ".png"):
                filename = ROOTDIR + str(i) + ".png"
                break

        result.writeToFile(filename, "png")

    def olivia_vh(self):
        while 1:
            base = device.takeSnapshot()

            still_auto_off = check_image(base, Elements.auto_off, tolerance=0.40)
            still_auto_on = check_image(base, Elements.auto_on, tolerance=0.70)
            still_phoebe_03 = check_image(base, Elements.phoebe_03_02)
            dc_dialog = check_image(base, Elements.dc_dialog)

            self.tap(Elements.phoebe_03_01, offset=30, timeout=0, spam=True)

            if dc_dialog:
                self.tap(Elements.dc_quit)
                MonkeyRunner.sleep(1)
                self.tap(Elements.yes_btn)
                return
            elif still_auto_off:  # This one bugs
                break
            # elif still_auto_on:
            #     self.tap(Elements.auto_on, offset=10, spam=True)
            else:
                self._device.touch(550, 1900, "DOWN")

        buffed = False

        # Shadow punch until dead
        punch_count = 0
        is_locked = False
        loop_count = 0
        while 1:
            base = device.takeSnapshot()
            still_phoebe_01 = check_image(base, Elements.phoebe_01_01, tolerance=0.4)
            still_phoebe_02 = check_image(base, Elements.phoebe_01_02, tolerance=0.55)
            still_roark_01 = check_image(base, Elements.roark_01_01)
            still_roark_02 = check_image(base, Elements.roark_01_02)
            dc_dialog = check_image(base, Elements.dc_dialog)

            if dc_dialog:
                self.tap(Elements.dc_quit)
                MonkeyRunner.sleep(1)
                self.tap(Elements.yes_btn)
                return
            elif still_roark_01 or still_roark_02:
                break
            # elif punch_count == 5 and is_locked is False:
            #     log("punching!")
            #     self.tap(Elements.phoebe_04_01, offset=30, timeout=0.25)
            #     is_locked = True
            elif still_phoebe_01 and (is_locked is False):
                self.tap(Elements.target_right, offset=30, timeout=0.1)
                self.tap(Elements.phoebe_01_01, offset=30, timeout=0, spam=True)
                punch_count = punch_count + 1
                is_locked = True
            elif still_phoebe_02:
                log("unlock!!")
                is_locked = False
            else:
                if loop_count % 10 == 0:
                    is_locked = False
                else:
                    loop_count += 1
                self._device.touch(550, 1900, "DOWN")

        buffed = False
        # Assume Roark
        while 1:
            log("Roark's Turn!")
            base = device.takeSnapshot()
            still_roark_01 = check_image(base, Elements.roark_01_01, 0.75)
            still_olivia_01 = check_image(base, Elements.olivia_01_01, 0.75)
            ok = check_image(base, Elements.ok)
            dc_dialog = check_image(base, Elements.dc_dialog)

            if dc_dialog:
                self.tap(Elements.dc_quit)
                MonkeyRunner.sleep(1)
                self.tap(Elements.yes_btn)
                return
            elif ok:
                return
            elif buffed is False:
                log("Roark Buff!")
                self.tap(Elements.roark_04_01, offset=30, timeout=0.25, spam=True)
                buffed = True
            elif still_roark_01:
                log("Roark Attack!")
                self.tap(Elements.roark_02_01, offset=30, timeout=0.25, spam=True)
                buffed = False
            elif still_olivia_01:
                break
            else:
                self._device.touch(225, 1900, "DOWN")

        # Assume Olivia
        hardened = False
        while 1:
            log("Olivia's Turn!")
            base = device.takeSnapshot()
            still_olivia_01 = check_image(base, Elements.olivia_01_01)
            olivia_sync = check_image(base, Elements.olivia_sync_01, tolerance=0.40)
            ok = check_image(base, Elements.ok)
            dc_dialog = check_image(base, Elements.dc_dialog)

            if dc_dialog:
                self.tap(Elements.dc_quit)
                MonkeyRunner.sleep(1)
                self.tap(Elements.yes_btn)
                return
            elif ok:
                return
            elif olivia_sync:
                self.tap(Elements.olivia_sync_01, offset=30, timeout=0.25, spam=True)
            elif hardened is False:
                self.tap(Elements.olivia_04_01, offset=30, timeout=0.25, spam=True)
                hardened = True
            elif still_olivia_01:
                self.tap(Elements.olivia_02_01, offset=30, timeout=0.25, spam=True)
            else:
                # Fallback to tap??
                self.tap(Elements.olivia_sync_01, offset=30, timeout=0.25, spam=True)
                # self._device.touch(220, 1900, "DOWN")


def kill_monkey(signum, frame):
    subprocess.call(["./kill_monkey.sh"])
    sys.exit(1)


if __name__ == "__main__":
    # Connects to the current device, returning a MonkeyDevice object
    # signal.signal(signal.SIGINT, kill_monkey)
    device = MonkeyRunner.waitForConnection()
    device.touch(0, 0, "DOWN")

    pkm = PokemonMastersBot(device)

    win_count = 0
    lose_count = 0

    selected_game = getattr(Elements, sys.argv[1])
    # Prep the game
    pkm.prep_game(True, selected_game)
    # pkm.wait_until(selected_game)
    # pkm.wait_until(Elements.coop_quick)

    play_times = []

    # Game Loop
    while 1:
        # Matching Room
        if "coop" in selected_game.url:
            btn_no = False
            while 1:
                base = device.takeSnapshot()

                go = check_image(base, Elements.go)
                m1 = check_image(base, Elements.matching_room_01, tolerance=0.40)
                m2 = check_image(base, Elements.matching_room_02, tolerance=0.40)
                r1 = check_image(base, Elements.not_enough_npc)

                if go:
                    pkm.tap(Elements.go)
                    MonkeyRunner.sleep(7)
                elif m1:
                    MonkeyRunner.sleep(1)

                elif m2 or r1:
                    if r1 and btn_no is False:
                        pkm.tap(Elements.no_btn)
                        btn_no = True
                    elif r1 and btn_no:
                        pkm.tap(Elements.yes_btn)
                        btn_no = False
                    else:
                        pkm.tap(Elements.no_btn)
                else:
                    log("Exit!")
                    break
        else:
            pkm.tap_n_wait(Elements.go, Elements.go)

        win, game_time = pkm.play_game(selected_game)
        play_times.append(game_time)

        if win:
            win_count += 1
        else:
            lose_count += 1

        log("Score Count: [" + str(win_count) + ":" + str(lose_count) + "]")
        log("Average Win Rate: " + str(win_count / (win_count + lose_count)))
        log("Average Lose Rate: " + str(lose_count / (win_count + lose_count)))
        log("Average Game Time: " + str(sum(play_times) / len(play_times)))

        if "coop" not in selected_game.url:
            if win:
                pkm.tap(Elements.battle_again)
            else:
                pkm.prep_game(False, selected_game)
        else:
            if win:
                pkm.tap(Elements.battle_again)
               
            pkm.prep_game(False, selected_game)
            
