#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent the attributes of a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Init a new instance of Square given a size.
        Args:
            size (int): Size of one side of the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter and setter for position."""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """A custom print function using the # character."""
        for x in range(self.__position[1]):
            print()
        for row in range(self.__size):
            [print(" ", end='') for y in range(self.__position[0])]
            [print("#", end='') for column in range(self.__size)]
            print()
        if self.__size == 0:
            print()
