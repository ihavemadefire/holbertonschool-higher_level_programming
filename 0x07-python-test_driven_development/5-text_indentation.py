#!/usr/bin/python3
"""this module contains a function that indents text."""


def text_indentation(text):
    """This Function indents text.

    Args:
        text to be parsed.

    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    q = [".", "?", ":"]
    i = 0
    while i < len(text):
        if text[i] in q:
            print("{:s}".format(text[i]))
            print()
            if text[i + 1] == " ":
                i += 1
        else:
            print("{:s}".format(text[i]), end='')
        i += 1
