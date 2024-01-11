#!/usr/bin/python3
"""
base_geometry module is a part of alx python oop and inheritance tasks.
It contains a class called BaseGeometry
"""


class BaseGeometry:
    """
    This class contains some basic features that any basic geometric shape has.
    It acts as a parent class for classes like "Rectangle", "Square", etc...
    """

    def area(self):
        """
        A method to calculate the area that will be overriden by
        sub classes
        """
        raise Exception("area() is not implemented")
