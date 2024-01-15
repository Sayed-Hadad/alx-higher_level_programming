#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes of the Square."""
        attributes = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

# Add a newline at the end of the file
