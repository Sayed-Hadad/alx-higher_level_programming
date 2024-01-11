#!/usr/bin/python3
""" A part of alx tasks on oop """


class Rectangle:
    """ A rectangle class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ an initializer for any object of type Rectangle """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ getter for the width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for the width attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter for the height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for the height attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of the rectangle """
        return self.height * self.width

    def perimeter(self):
        """ returns the perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """ string representation of Rectangle objects """
        if self.width == 0 or self.height == 0:
            return ""
        st = ''
        for i in range(self.height):
            st += str(self.print_symbol) * self.width
            st += '\n'
        return st.strip()

    def __repr__(self):
        """ an offictial string representation for Rectangle """
        return f'Rectangle({self.width}, {self.height})'

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the Rectangle with the bigger area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """ returns a rectangle with width = height = size """
        return cls(size, size)

    def __del__(self):
        """ deleting Rectangle object """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
