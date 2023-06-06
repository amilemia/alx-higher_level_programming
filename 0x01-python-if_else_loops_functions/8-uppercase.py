#!/usr/bin/python3


def uppercase(string):
    for char in string:
        if ord('a') <= ord(char) <= ord('z'):
            print("{:c}".format(ord(char) - 32), end='')
        else:
            print("{:c}".format(ord(char)), end='')
    print()
