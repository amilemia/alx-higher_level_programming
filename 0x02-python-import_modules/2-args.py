#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1

    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc == 1:
        print("{} argument:".format(argc))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(argc))
        for i in range(1, argc + 1):
            print("{}: {}".format(i, argv[i]))
