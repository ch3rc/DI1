"""
Author:     Cody Hawkins
Date:       September 3,2020
Class:      5420
File:       fileinfo.py
Project:    Assignment one
"""
import os
import imghdr
import cv2 as cv


def get_size(file):
    # get file size and return size of file in GIGs, MBs, KBs or Bytes
    GIG = 1073741824
    MB = 1048576
    KB = 1024
    size = None
    file_size = os.path.getsize(file)
    if file_size >= GIG:
        size = "{:.2f}GB".format(file_size / GIG)
        return size
    elif (file_size < GIG) and (file_size >= MB):
        size = "{:.2f}MB".format(file_size / MB)
        return size
    elif (file_size < MB) and (file_size >= KB):
        size = "{:.2f}KB".format(file_size / KB)
        return size
    else:
        size = "{}Bytes".format(file_size)
        return file_size


def pic_info(file, i):
    # Display pic info to terminal
    size = get_size(file)
    i_t = imghdr.what(file)
    i_name = os.path.basename(file)
    i_path = os.path.abspath(file)
    img = cv.imread(i_path)
    file_size = os.path.getsize(file)
    """
    In order for printout: pic number starting from 0, image type, image shape including RGB or grey,
    image size, full path of where image is stored, file size formated to 2 decimal places, image name
    """
    print("{}: {}, {}, ({}), {}, {}, {} ".format(i, i_t, img.shape, img.size, i_path, size, i_name))
