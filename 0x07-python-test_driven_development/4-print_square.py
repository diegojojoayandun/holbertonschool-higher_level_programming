#!/usr/bin/python3
"""Module Print a Square
"""

def print_square(size):
    """prints a square with the character #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(0, size):
            print('#'.format(), end="")
        print()
