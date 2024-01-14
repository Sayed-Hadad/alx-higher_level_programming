#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle object."""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.height}"

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width
    
    @width.setter
    def width(self, w):
        """Set the width of the Rectangle."""
        if not isinstance(w, int):
            raise TypeError("width must be an integer")
        elif w <= 0:
            raise ValueError("width must be > 0")
        self.__width = w

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height
    
    @height.setter
    def height(self, h):
        """Set the height of the Rectangle."""
        if not isinstance(h, int):
            raise TypeError("height must be an integer")
        elif h <= 0:
            raise ValueError("height must be > 0")
        self.__height = h

    @property
    def x(self):
        """Get the x-coordinate of the Rectangle."""
        return self.__x
    
    @x.setter
    def x(self, x):
        """Set the x-coordinate of the Rectangle."""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
    
    @property
    def y(self):
        """Get the y-coordinate of the Rectangle."""
        return self.__y
    
    @y.setter
    def y(self, y):
        """Set the y-coordinate of the Rectangle."""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
    
    def area(self):
        """Calculate the area of the Rectangle."""
        return self.__width * self.__height

    def display(self):
        """Display the Rectangle by printing '#' characters."""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args):
        """Update attributes of the Rectangle."""
        attributes = ["id", "width", "height", "x", "y"]
        for i in range(len(args)):
            setattr(self, attributes[i], args[i])
