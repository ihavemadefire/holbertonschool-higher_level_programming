#!/usr/bin/python3
"""This module contains a function"""


def append_write(filename="", text=""):
    """This function writes to file"""
    with open(filename, 'a', encoding="utf-8") as file:
        nb_characters = file.write(text)
    return nb_characters
