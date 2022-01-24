#!/usr/bin/python3
"""Module 1-rectangle
Defines a Rectangle class.
"""


class Rectangle:
    """Rectangle class, with width and height."""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.
            width: rectangle width
            height: rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width
        value: value of the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height
        value: value of the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates area of rectangle
         with width and height """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a Rectangle instance
        Returns: Perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns an informalstring representation
        of this classs, filled with '#'"""
        if self.__height == 0 or self.__width == 0:
            return ''
        result = ''
        for i in range(self.__height):
            for j in range(self.__width):
                result += '#'
            result += '\n'
        return result[:-1]

    def __repr__(self):
        """returns repr formal of rectangle instance"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes a Rectangle instance."""
        print("Bye rectangle...")
