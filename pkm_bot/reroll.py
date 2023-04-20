from pkm_types import Location
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage


_device = MonkeyRunner.waitForConnection()


def tap(x, y):
    print("{" + str(x) + "," + str(y) + "}")
    _device.touch(x, y, "DOWN_AND_UP")
    MonkeyRunner.sleep(2)


def drag(src, dst):
    _device.drag(src, dst, 0.5, 20)
    MonkeyRunner.sleep(1)


def tap_n_wait(count):

    for i in range(count):
        tap(430, 1279)
        print("n_wait: {" + str(i) + "}")


def wait(i):
    MonkeyRunner.sleep(i)


def spam(loc, n):
    if n == 4:
        return
    print(n)
    tap(loc[0],loc[1])
    spam((loc[0] + 10, loc[1] + 10), n + 1)
    spam((loc[0] - 10, loc[1] + 10), n + 1)
    spam((loc[0] + 10, loc[1] + 10), n + 1)
    spam((loc[0] - 10, loc[1] + 10), n + 1)

tap(571, 1047)
wait(2)
tap(571, 1047)
tap(516, 1308)  # OK
drag((286, 1113), (286, 1013))
drag((593, 1113), (593, 1013))
drag((824, 1113), (824, 1013))
tap(576, 1607)  # OK
tap(166, 1278)
tap(166, 1418)
tap(576, 1607)  # OK
wait(5)
tap(576, 1607)  # OK
tap(641, 1260)
tap(479, 1505)
print("Downloading data")
tap(641, 1260)
wait(10)
tap(641, 1260)
tap(641, 1260)
tap(641, 1260)
tap(430, 1279)
tap(430, 1279)  # Game will restart?
tap(430, 1279)
### - GARY SPEECH
wait(5)  #
tap_n_wait(5)
wait(10)
tap(349, 957)
print("typing the data now")
_device.type("a\n")
wait(2)
tap(430, 1279)
wait(3)
tap(468, 1803)  # NEXT
tap(468, 1803)  # NEXT
tap(468, 1803)  # NEXT
tap(468, 1803)  # NEXT
tap(764, 1292)
tap_n_wait(15)
wait(15)
spam((522, 754), 1)
tap_n_wait(30)
tap(522, 1476)
tap(522, 1476)
tap(522, 1476)
tap(522, 1476)
tap(522, 1476)
tap(522, 1476)
tap(56, 354)  # Check point!
### - First Battle Battle
wait(2)
tap(484, 1681)
tap(484, 1681)
wait(1)
tap(56, 354)
tap(56, 354)
tap(56, 354)
wait(3)
tap(541, 1643)
tap(541, 1643)
tap(541, 1643)
wait(3)
tap(428, 261)  # mission loc
wait(3)
tap_n_wait(50)
tap(334, 1744)  # ok
wait(5)
### - Second Battle
wait(5)
tap(428, 261)  # mission loc
tap(428, 261)  # mission loc
tap(428, 261)  # mission loc
wait(1)
tap(318, 1751)  # go
tap_n_wait(12)
wait(4)
tap_n_wait(10)
tap(434, 1500)  # pika attack
wait(3)
tap(77, 1589)  # tap brock
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap_n_wait(8)
wait(2)
tap_n_wait(8)
wait(4)
tap_n_wait(10)
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(903, 401)  # E3
tap(903, 401)  # E3
tap(903, 401)  # E3
tap(903, 401)  # E3
tap(903, 401)  # E3
tap(903, 401)  # E3
tap(903, 401)  # E3
tap(903, 401)  # E3
tap(903, 401)  # E3
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(77, 1589)  # tap brock
tap(77, 1589)  # tap brock
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
wait(3)
tap_n_wait(20)
tap(334, 1744)  # ok
wait(5)
#### MISSION 3!
tap(428, 261)  # mission loc
tap_n_wait(50)
wait(5)
tap(334, 1744)  # ok
wait(5)
#### MISSION 4!
tap(428, 261)  # mission loc
wait(1)
tap(318, 1751)  # go
tap(318, 1751)  # go
wait(6)
tap_n_wait(8)
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(525, 1589)  # Sync attack pika
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(525, 1589)  # Sync attack pika
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(525, 1589)  # Sync attack pika
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(525, 1589)  # Sync attack pika
tap(434, 1500)  # pika attack
tap(525, 1589)  # Sync attack pika
tap(525, 1589)  # Sync attack pika
tap(525, 1589)  # Sync attack pika
tap(525, 1589)  # Sync attack pika
tap(525, 1589)  # Sync attack pika
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(525, 1589)  # Sync attack pika
tap(525, 1589)  # Sync attack pika
tap(525, 1589)  # Sync attack pika
tap(525, 1589)  # Sync attack pika
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(434, 1500)  # pika attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap(155, 1487)  # brock attack
tap_n_wait(25)
tap(334, 1744)  # ok
tap(334, 1744)  # ok
tap(334, 1744)  # ok
tap(334, 1744)  # ok
tap(334, 1744)  # ok
wait(5)
### MISSION 6
wait(5)
tap(428, 261)  # mission loc
tap_n_wait(10)
tap(334, 1744)
tap(334, 1744)
tap(334, 1744)
tap(334, 1744)
tap_n_wait(15)
tap(334, 1744)  # ok
tap(334, 1744)  # ok
wait(4)
tap_n_wait(40)
wait(20)
## ROLL
spam((334, 1744), 1)
tap_n_wait(5)
tap(354, 314)  # select scout
tap(354, 314)
wait(3)
tap(452, 1520)
tap(452, 1520)
tap(452, 1520)
wait(4)
drag((544, 596), (536, 1677))
tap_n_wait(10)
tap(498, 1615)  # ok
tap(498, 1615)  # ok
tap(498, 1615)  # ok
tap_n_wait(2)
tap(728, 1781)
tap(728, 1781)
wait(4)
tap(354, 314)
tap(354, 314)
tap(354, 314)
tap(863, 773)
tap(863, 773)
tap(863, 773)
tap(184, 1265)
tap(184, 1265)
tap(184, 1265)
tap(334, 1744)  # ok
tap(334, 1744)  # ok
tap_n_wait(10)
tap(548, 1283)
tap(548, 1283)
tap(548, 1283)
