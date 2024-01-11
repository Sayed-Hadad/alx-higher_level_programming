#!/usr/bin/python3
"""
rectangle module is a part of alx python oop and inheritence tasks.
It inherits the BaseGeometry class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    The Rectangle class is a sub-class of the BaseGeometry class.
    It will be used to define the specific attributes and methods
    needed to create a Rectangle object
    """

    def __init__(self, width, height, name_1="width", name_2="height"):
        """
        init method that sets the private attributes (width, height)
        to the passed args width and height after validating that the
        passed args are +ve
        """
        self.integer_validator(name_1, width)
        self.integer_validator(name_2, height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Implementation of the area function for the
        Rectangle class
        """
        return self.__width * self.__height

    def __str__(self, name='Rectangle'):
        """
        returns an informal description of the Rectangle objects
        """
        return f"[{name}] {self.__width}/{self.__height}"
