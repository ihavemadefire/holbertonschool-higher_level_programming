#!/usr/bin/python3
"""This module contains the class BaseGeometry"""


class Rectangle():
    """This is the class BaseGeometry"""
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__value = self.integer_validator("height", height)

    def area(self):
        """This is the area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This is a validator function"""
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
        else:
            self.__name = name
            self.__value = value
