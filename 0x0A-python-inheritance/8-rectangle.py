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

    def __init__(self, width, height):
        """
        init method that sets the private attributes (width, height)
        to the passed args width and height after validating that the
        passed args are +ve
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
