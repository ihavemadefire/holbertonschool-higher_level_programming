#!/usr/bin/python3
"""This module contains the class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is the class BaseGeometry"""
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__width = width
        self.__value = self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """This is the area function"""
        raise Exception("area() is not implemented")
