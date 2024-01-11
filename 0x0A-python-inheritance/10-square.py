#!/usr/bin/python3
"""
square module: it's a part of alx oop and inheritence tasks.
It's a sub-class of Rectangle class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This is a sub-class of the class Rectangle
    It will be used to define the specific attributes and methods
    needed to create a Rectangle object
    """
    def __init__(self, size):
        """
        init method: set the private attribute size to the passed
        argument size after validating that it's +ve
        """
        super().__init__(size, size, "size", "size")
        self.__size = size

    def area(self):
        """
        Implementing the area for the class Square using
        the parent implementation
        """
        return super().area()
