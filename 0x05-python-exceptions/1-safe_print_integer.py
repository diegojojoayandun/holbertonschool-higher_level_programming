#!/usr/bin/python3
'''Safe printing of integers list'''


def safe_print_integer(value):
    ''' prints an integer with "{:d}".format().'''
    try:
        print('{:d}'.format(value))
        return True
    except ValueError:
        return False
