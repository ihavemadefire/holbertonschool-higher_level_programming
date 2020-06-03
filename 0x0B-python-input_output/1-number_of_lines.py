#!/usr/bin/python3
"""This module contains a single function"""


def number_of_lines(filename=""):
    """This file returns a count of lines in a file"""
    count = 0
    with open(filename) as file:
        for line in file:
            count += 1
    return count
