"""
Author:     Cody Hawkins
Date:       September 3,2020
Class:      5420
File:       dfs.py
Project:    Assignment one
"""
import os
import sys
import cv2 as cv
import numpy as np


def DFS(base, ignore=True):
    child = os.listdir(base)

    for name in child:
        fullpath = os.path.join(base, name)
        if os.path.isdir(fullpath) and not (ignore and os.path.islink(fullpath)):
            for (next_base, next_child) in DFS(fullpath, ignore):
                yield next_base, next_child

    yield base, child


def Run(file_path):
    holder = []
    path = file_path
    for (base, child) in DFS(base=path):
        for name in child:
            tmp = os.path.join(base, name)
            tmp = os.path.abspath(tmp)
            try:
                img = cv.imread(tmp)
                if type(img) is np.ndarray:
                    holder.append(tmp)
            except Exception as err:
                print(err)
                sys.exit(1)
    return holder
