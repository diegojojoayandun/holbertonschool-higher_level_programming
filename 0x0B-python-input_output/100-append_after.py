#!/usr/bin/python3
"""Module 100-append_after Inserts a line of text to a file,
after each line containing a specific string"""


import re
def append_after(filename="", search_string="", new_string=""):
    """Appends the new_string after
    the search_string in filename"""

    with open(filename, "r") as f:
        text = f.readlines()

    _match =  re.compile(search_string)

    with open(filename, "w") as f1:
        s = ""
        for line in text:
            s += line
            if  _match.match(line):
                s += new_string
        f1.write(s)
