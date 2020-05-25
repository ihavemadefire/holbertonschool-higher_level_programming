#!/usr/bin/python3
"""This module defines a class of Rectangle"""


class Rectangle:
    """This class defines a rectangle

    Args:
        width (int): width of rectangle
        height (int): height of rectangle

    """
    def __init__(self, width=0, height=0):
        """Initialization function"""
        self.width = width
        self.height = height

    def area(self):
        """This method returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """This method returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    @property
    def width(self):
        """Getter and setter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter and setter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """Produces printed string"""
        if self.__height == 0 or self.__width == 0:
            return ''
        rectangle = []
        for i in range(self.__height):
            [rectangle.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """Produces repr to be used by eval"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Deletes instance and prints a message"""
        print("Bye rectangle...")
