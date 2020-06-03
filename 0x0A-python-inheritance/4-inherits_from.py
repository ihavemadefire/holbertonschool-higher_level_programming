#!/usr/bin/python3
"""This is yet another module"""


def inherits_from(obj, a_class):
    """detemines if subclass only"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
