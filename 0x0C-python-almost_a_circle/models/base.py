#!/usr/bin/python3
"""module base - this class will be tha base
of all other classes for this project
"""


class Base:
    """This class will be the “base” of all other classes in this project.
    """

    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """Initializes the data with validation"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
