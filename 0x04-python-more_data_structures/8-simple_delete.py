#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if type(key) == str:
        del a_dictionary[key]
    return a_dictionary
