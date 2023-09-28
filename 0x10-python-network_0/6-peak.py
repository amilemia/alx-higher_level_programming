#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None

    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]

    mid = length // 2
    mid_value = list_of_integers[mid]

    if (mid == length - 1 or mid_value >= list_of_integers[mid + 1]) and (
        mid == 0 or mid_value >= list_of_integers[mid - 1]
    ):
        return mid_value

    if mid != length - 1 and list_of_integers[mid + 1] > mid_value:
        return find_peak(list_of_integers[mid + 1:])

    return find_peak(list_of_integers[:mid])
