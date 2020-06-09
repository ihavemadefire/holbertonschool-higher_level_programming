#!/usr/bin/python3
"""This module contains a class called rectangle"""
from models.base import Base


class Rectangle(Base):
    """This class is for rectangles"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization function"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def update(self, *args, **kwargs):
        """This is an update function"""
        if len(args) > 0:
            if len(args) >= 1:
                super().__init__(args[0])
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            if kwargs.get('id'):
                super().__init__(kwargs.get('id'))
            if kwargs.get('width'):
                self.width = kwargs.get('width')
            if kwargs.get('height'):
                self.height = kwargs.get('height')
            if kwargs.get('x'):
                self.x = kwargs.get('x')
            if kwargs.get('y'):
                self.y = kwargs.get('y')

    def area(self):
        """Returns area"""
        return self.width * self.height

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.x, self.y, self.width, self.height))

    def display(self):
        """Prints rectangle"""
        [print() for i in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for i in range(self.x)]
            [print("#", end="") for j in range(self.width)]
            print()

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def to_dictionary(self):
        """Creates a dictionary representation"""
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'width': self.width,
            'height': self.height}
