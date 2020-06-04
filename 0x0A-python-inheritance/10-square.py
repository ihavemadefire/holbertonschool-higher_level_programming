#!/usr/bin/python3
"""Docstring"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """It's hip to be square"""
    def __init__(self, size):
        """Would you like to supersize?"""
        super().__init__(size, size)
