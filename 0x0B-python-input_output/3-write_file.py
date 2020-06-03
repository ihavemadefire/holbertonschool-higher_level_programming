#!/usr/bin/python3
"""This module contains a funtion or two"""


def write_file(filename="", text=""):
    """This function writes to file"""
    with open(filename, 'w', encoding="utf-8") as file:
        nb_characters = file.write(text)
    return nb_characters
