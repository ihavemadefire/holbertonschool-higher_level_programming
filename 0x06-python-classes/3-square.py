#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent the attributes of a square."""
    def __init__(self, size=0):
        """Init a new instance of Square given a size.
        Args:
            size (int): Size of one side of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of a square."""
        return self.__size ** 2
