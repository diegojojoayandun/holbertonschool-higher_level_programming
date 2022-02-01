#!/usr/bin/python3
"""module 0-read_file
    Args: filename: the path or name of a file
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints
    it to stdout"""

    with open(filename) as f:
        _read_file = f.read()
        print(_read_file)
        f.close
