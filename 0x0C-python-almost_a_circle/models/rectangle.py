#!/usr/bin/python3
"""
This is a part of alx python tasks.
This module contains a class called Rectangle
that inherits from a class called Base
"""

from .base import Base


class Rectangle(Base):
    """
    Rectangle class is a sub-class that inherites from
    the Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing objects of type rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """getter for heigh"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """return the area of the rectangle object"""
        return self.height * self.width

    def display(self):
        """Display the rectangle using '#' char"""
        if self.y:
            vertical_space = '\n' * (self.y - 1)
            print(vertical_space)
        displayed_line = (' ' * self.x) + ('#' * self.width)
        for i in range(self.height):
            print(displayed_line)

    def __str__(self, name='Rectangle'):
        """Inforaml representation of the Rectangle object."""
        return (f'[{name}] ({self.id}) {self.x}/{self.y} ' +
                f'- {self.width}/{self.height}')

    def update(self, *args, **kwargs):
        """
        update the rectangle object by
        assigning an argument to each attribute
        """
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.width = args[i]
            elif i == 2:
                self.height = args[i]
            elif i == 3:
                self.x = args[i]
            elif i == 4:
                self.y = args[i]
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @classmethod
    def dummy(cls):
        """
        A function that creates a dummy object to be updated within
        create method using json data
        """
        return cls(10, 10)

    def to_dictionary(self):
        """returns a dictionary representation of rectangle objects"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
