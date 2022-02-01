#!/usr/bin/python3
"""Module 5-save_to_json_file
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes the representation of my_obj to filename.
    """

    with open(filename, 'w+') as f:
        json.dump(my_obj, f)
