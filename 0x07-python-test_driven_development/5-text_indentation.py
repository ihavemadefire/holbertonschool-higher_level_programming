#!/usr/bin/python3
"""this module contains a function that indents text."""


def text_indentation(text):
    """This Function indents text"""
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    q = [".", "?", ":"]

    for i in range(len(text)):
        if text[i] in q:
            print("{:s}".format(text[i]), end='')
            print()
            print()
        else:
            print("{:s}".format(text[i]), end='')
