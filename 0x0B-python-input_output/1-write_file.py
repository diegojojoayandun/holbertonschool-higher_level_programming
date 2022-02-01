#!/usr/bin/python3
"""module 1-write_file - use of IO write
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    returns: the number of characters written"""

    with open(filename, 'w+') as f:
        file = f.write(text)
        f.close
        return file
