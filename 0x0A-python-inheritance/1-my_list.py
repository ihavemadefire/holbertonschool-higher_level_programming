#!/usr/bin/python3
"""This module contains a class called MyList"""


class MyList(list):
    """This is a subclass of list"""
    def __init__(self):
        """Initialization function"""
        super().__init__()

    def print_sorted(self):
        """Sorted print method"""
        a = self[:]
        a.sort(reverse=False)
        print(a)
