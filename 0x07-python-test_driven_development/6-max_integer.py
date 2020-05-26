#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find the maximum integer in a list
        If the list is empty, it returns None
    """
    if len(list) == 0:
        return None
    for i in list:
        if not isinstance(i, int):
            return
    list.sort(reverse=True)
    return list[0]
