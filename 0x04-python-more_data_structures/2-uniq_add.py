#!/usr/bin/python3
def uniq_add(my_list=[]):

    """
    Add all unique
    integers in a list
    """
    uniq_list = []
    add = 0
    for num in my_list:
        if num not in uniq_list:
            add += num
            uniq_list.append(num)
    return add
