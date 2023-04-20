import sys

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from bot_types import Elements
from os.path import splitext


def replace(base_url,target):
    base = MonkeyRunner.loadImageFromFile(base_url)
    sub_image = base.getSubImage((target.x, target.y, target.width, target.height))
    file_name = splitext(target.url)[0] + ".png"
    sub_image.writeToFile("images/"+ file_name,"png")
    return True

if __name__ == "__main__":
    base = sys.argv[1]
    target = getattr(Elements,sys.argv[2])
    replace(base,target)