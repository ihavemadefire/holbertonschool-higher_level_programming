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

    def my_print(self):
        """A custom print function using the # character."""
        for row in range(0, self.__size):
            [print("#", end='') for column in range(0, self.__size)]
            print()
        if self.__size == 0:
            print()
