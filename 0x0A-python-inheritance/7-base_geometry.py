#!/usr/bin/python3
"""This module contains the class BaseGeometry"""


class BaseGeometry():
    """This is the class BaseGeometry"""
    def area(self):
        """This is the area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This is a validator function"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
