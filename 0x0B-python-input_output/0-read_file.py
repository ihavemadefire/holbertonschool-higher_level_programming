#!/usr/bin/python3
"""This module contains a readfile function"""

def read_file(filename=""):
    """This function prints a file"""
    with open(filename) as file:
        print(file.read(), end="")
