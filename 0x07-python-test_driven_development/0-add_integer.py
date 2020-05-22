#!/usr/bin/python3
"""This module contains an add def."""


def add_integer(a, b=98):
    """This function adds two ints or floats and returns an int"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
