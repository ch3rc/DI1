"""
Author:     Cody Hawkins
Date:       September 3,2020
Class:      5420
File:       main.py
Project:    Assignment one
"""
import getopt, sys, os
import dfs
from display import display_image


def help():
    """ help message with prompts """
    print("\t---HELP MESSAGE--\n")
    print("-h: prints help menu")
    print("-r: number of rows")
    print("-c: number of columns")
    print("Provide a file path at the end or the directory name will default to cwd\n")
    print("While program is running spacebar or n to see next image")
    print("P will display previous image and q will exit the program")


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hr:c:", ["help", "rows", "columns"])
    except getopt.GetoptError as err:
        print(err)
        sys.exit()
    rows = 720
    columns = 1080
    dirname = os.getcwd()
    for o, a in opts:
        if o in ("-h", "--help"):
            help()
            sys.exit(0)
        elif o in ("-r", "--rows"):
            rows = a
        elif o in ("-c", "--columns"):
            columns = a
        else:
            assert False, "unhandled option"

    for a in args:
        if a is not None:
            dirname = a
    
    if os.path.exists(dirname):
        files = dfs.Run(dirname)
        display_image(files, rows, columns)
    else:
	print("Path does not exist")
	sys.exit(1)


if __name__ == "__main__":
    main()
