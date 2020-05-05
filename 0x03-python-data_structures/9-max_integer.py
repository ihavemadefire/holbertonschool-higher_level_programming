#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1 or my_list is None:
        return
    my_list.sort()
    a = my_list[-1]
    return a
