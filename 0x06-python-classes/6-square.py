#!/usr/bin/python3
""" Defining a square class """


class Square:
    """ handling the private size attribute to the square class """

    def __init__(self, size=0, position=(0, 0)):
        """ initializing the square object """
        self.size = size
        self.position = position

    def area(self):
        """ calculating the area of the square """

        return self.__size * self.__size

    @property
    def size(self):
        """ property function size """
        return self.__size

    @property
    def position(self):
        """ property function for position attribute """
        return self.position

    @size.setter
    def size(self, value):
        """ setter function """
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    @position.setter
    def position(self, value):
        if len(value) != 2 or not isinstance(value, tuple) or \
                not all(isinstance(num, int) for num in value) or\
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ printing the square using # character """
        if self.__size == 0:
            print('')
        else:
            for i in range(self.__position[1]):
                print('')
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
