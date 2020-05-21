#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent the attributes of a square."""
    def __init__(self, size=0):
        """Init a new instance of Square given a size.
        Args:
            size (int): Size of one side of the square.
        """
        self.size = size

    def area(self):
        """Returns the area of a square."""
        return self.__size ** 2

    @property
    def size(self):
        """Getter and setter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """Returns the == value of two squares"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Returns the != value of two squares"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Returns the < value of two squares"""
        return self.area() < other.area()

    def __le__(self, other):
        """Returns the <= value of two squares"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Returns the > value of two squares"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Returns the >= value of two squares"""
        return self.area() >= other.area()
