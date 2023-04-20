import sys
import cv2
import numpy as np
from os.path import basename, splitext, dirname


def check_image(base_image, target_image):
    image = cv2.imread(base_image)
    template = cv2.imread(target_image)
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    cv2_location = np.unravel_index(result.argmax(), result.shape)

    shape = template.shape

    print(
        str(shape[0])
        + ", "
        + str(shape[1])
        + ", "
        + str(cv2_location[1])
        + ", "
        + str(cv2_location[0])
    )

    # print(cv2_location)
    # print(shape)


if __name__ == "__main__":

    if len(sys.argv) == 3:
        base = sys.argv[1]
        target = sys.argv[2]
    else:
        base = sys.argv[1]
        filename = splitext(basename(base))
        target = dirname(base) + "/" + filename[0] + ".jpeg"

    check_image(base, target)
