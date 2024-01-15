#!/usr/bin/python3
"""
This is a part of alx python tasks.
This module contains a class called Square
that inherits from a class called Rectangle
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """
    Square class is a sub-class that inherits from the
    Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the Square objects"""
        super().__init__(size, size, x, y, id)

    def __str__(self, name='Square'):
        """Informal Representation of the Square objecs"""
        return (f'[{name}] ({self.id}) {self.x}/{self.y} ' +
                f'- {self.width}')

    @property
    def size(self):
        """Getter for the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for the size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update the square object by
        assigning an argument to each attribute
        """
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.size = args[i]
            elif i == 2:
                self.x = args[i]
            elif i == 3:
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
        return cls(10)

    def to_dictionary(self):
        """
        A method that returns the dictionary
        representation of a Square
        """
        sq_dic = super().to_dictionary()
        sq_dic['size'] = sq_dic.pop('width')
        sq_dic.pop('height')
        return sq_dic
