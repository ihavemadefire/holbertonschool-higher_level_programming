#!/usr/bin/python
"""This module contains a function called Print_Square."""


def print_square(size):
    """This function prints squares.

    Args:
        size: sixe of one side of the square.

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()
    else:
        for row in range(size):
            [print("#", end='') for column in range(size)]
            print()
