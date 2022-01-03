#!/usr/bin/python3
def no_c(my_string):
    translation = my_string.maketrans({ord('C'): None, ord('c'): None})
    new_string = my_string.translate(translation)
    return new_string
