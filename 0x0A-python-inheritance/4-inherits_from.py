#!/usr/bin/python3
"""This is yet another module"""


def inherits_from(obj, a_class):
    """detemines if subclass only"""
    return issubclass(type(obj), a_class)
