#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
         super().__init__(size, size, x, y, id )
    def __str__(self):
        """Return a string representation of the Rectangle."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    
    @property 
    def size(self):
         """Get the size of the Square."""
         return self.width
    
    @size.setter
    def size(self , value):
         self.width = value
         self.height = value