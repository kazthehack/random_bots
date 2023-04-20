# Imports the monkeyrunner modules used by this program
import os
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

# Takes a screenshot
result = device.takeSnapshot()

# Writes the screenshot to a file
filename = None
ROOTDIR = "reroll/"
for i in range(1000):
    if not os.path.isfile(ROOTDIR + str(i) + ".png"):
        filename = ROOTDIR + str(i) + ".png"
        break

result.writeToFile(filename,'png')