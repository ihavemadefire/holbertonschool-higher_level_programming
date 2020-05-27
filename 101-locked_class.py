#!/usr/bin/python3
"""Doctring"""


class LockedClass:
    """docstring"""
    def __init__(self, first_name=""):
        self.first_name = first_name

    __slots__ = ['first_name']
