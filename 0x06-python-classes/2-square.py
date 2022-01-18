#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """defines a square
    Private instance attribute: size
    Instantiation with optional size:
        -def __init__(self, size=0):
    """


    def __init__(self, size=0):
        """Initializes the data with validation"""
        if not  type(size) == int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        self.__size = size
