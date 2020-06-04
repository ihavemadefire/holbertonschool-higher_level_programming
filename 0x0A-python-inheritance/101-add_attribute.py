#!/usr/bin/python3
"""Docstring"""


def add_attribute(obj, name, value):
    """Docstring"""
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
