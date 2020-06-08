#!/usr/bin/python3
"""This module contains a class called Base"""


class Base():
    """"This is the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """This is an initialization method"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
