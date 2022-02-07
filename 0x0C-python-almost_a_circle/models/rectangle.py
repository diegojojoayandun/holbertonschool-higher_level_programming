#!/usr/bin/python3
"""Module rectangle.
Create a Rectangle class, inheriting from Base."""


from models.base import Base


class Rectangle(Base):
    """class Rectangle
    defines a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes a rectangle class instance"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
