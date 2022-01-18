#!/usr/bin/python3
"""defines a square"""


class Square:
    """defines a square
    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
    """
    def __init__(self, size=0):
        """Initializes the data with validation"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Square area."""
        return self.__size ** 2
