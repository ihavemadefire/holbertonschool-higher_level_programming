#!/usr/bin/python3
"""Defines a module magic_class."""

import math


class MagicClass:
    """Define a class for a circle.
    Arg: radius is the radius of the circle.
    """
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Returns the area of a circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns the circumferance of a circle."""
        return 2 * math.pi * self.__radius
