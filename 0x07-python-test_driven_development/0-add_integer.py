#!/usr/bin/python3
"""Module add-integer - adds 2 integers.
 a and b must be integers or floats, otherwise raise a TypeError
 exception with the message a must be an integer or b must be an integer
 a and b must be first casted to integers if they are float
"""


def add_integer(a, b=98):
    """Returns the addition of a and b,
    or an error if a and b are not integers or floats
    """
    if a == "":
        raise TypeError("a must be an integer")

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return (a + b)

print(add_integer(float('inf'), 0))
