#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1 or my_list is None:
        return
    a = 0
    for i in my_list:
        if i > a:
            a = i
    return a
