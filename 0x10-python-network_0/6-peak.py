#!/usr/bin/python3
"""This returns a peak"""


def find_peak(list_of_integers):
    """Returns a list"""
    a = list_of_integers
    l = len(list_of_integers)
    same = 0
    if l <= 2:
        return None
    if l == 2:
        return max(a)
    for i in range(1, l - 1):
        if a[i] != a[i + 1]:
            same = 1
        if a[i - 1] < a[i] and a[i + 1] < a[i]:
            return a[i]
    if same == 0:
        return a[0]
    return None
