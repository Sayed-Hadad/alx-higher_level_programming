#!/usr/bin/python3
""" Defining a square class """


class Square:
    """ handling the private size attribute to the square class """

    def __init__(self, size=0):
        """ initializing the square object """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ calculating the area of the square """

        return self.__size * self.__size

    @property
    def size(self):
        """ property function size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter function """
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
