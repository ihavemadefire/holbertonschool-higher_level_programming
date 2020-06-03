#!/usr/bin/python3
"""This module contains a class called MyList"""


class MyList(list):
    """This is a subclass of list"""

    def print_sorted(self):
        """Sorted print method"""
        a = self[:]
        a.sort(reverse=False)
        return print(a)
