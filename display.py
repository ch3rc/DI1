"""
Author:     Cody Hawkins
Date:       September 3,2020
Class:      5420
File:       display.py
Project:    Assignment one
"""
import cv2
import os
import sys
from fileInfo import pic_info
import imutils


def display_image(file, rows, cols):
    """
    Files passed from the depth first search are sent over to
    this function where the image information is displayed and
    the user can interactively move between the next and previous
    images in the array provided

    The display window will be set to provided height and width.
    The image will then be resized accordingly to fit the window
    """
    i = 0
    while i < len(file):
        cv2.namedWindow("buffer", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("buffer", int(cols), int(rows))

        # abspath necessary to get imread() to work
        temp = os.path.abspath(file[i])
        pic_info(file[i], i)
        img = cv2.imread(temp)

        # imutils.resize resizes the image while retaining the aspect ration
        resized = imutils.resize(img, int(cols), int(rows))
        cv2.imshow("buffer", resized)

        while True:
            key = cv2.waitKey(0)
            # Move to next pic with 'space' or 'n'
            if key == 32 or key == 110:
                cv2.destroyWindow('buffer')
                i += 1
                break
            # Go to previous picture with 'p'
            if key == 112 and i is not 0:
                i -= 1
                cv2.destroyWindow('buffer')
                break
            # Destroy all windows and exit program with 'q'
            if key == 113:
                cv2.destroyAllWindows()
                sys.exit(0)
                break

    cv2.destroyAllWindows()
