#!/usr/bin/python3
class Square:
    """A square"""
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        for row in range(self.__size):
            [print("#", end='') for column in range(self.__size)]
            print()
        if self.__size == 0:
            print()