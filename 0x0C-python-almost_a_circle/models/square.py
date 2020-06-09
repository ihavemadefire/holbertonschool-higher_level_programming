#!/usr/bin/python3
"""This module stared into the abyss too long and now listens to Morrissey"""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """This is a subclass on square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization function"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """This is the size funtion"""
        return self.__width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value
        self.__heigth = value

    def update(self, *args, **kwargs):
        """Update"""
        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if kwargs.get('id'):
                self.id = (kwargs.get('id'))
            if kwargs.get('size'):
                self.size = kwargs.get('size')
            if kwargs.get('x'):
                self.x = kwargs.get('x')
            if kwargs.get('y'):
                self.y = kwargs.get('y')

    def __str__(self):
        """This is the str rep function"""
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.size))

    def to_dictionary(self):
        """This is a def"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
