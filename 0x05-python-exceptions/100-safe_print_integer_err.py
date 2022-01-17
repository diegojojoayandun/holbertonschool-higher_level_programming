#!/usr/bin/python3
'''Safe printing of integers list'''


import sys


def safe_print_integer_err(value):
    ''' prints an integer with "{:d}".format().'''
    try:
        print('{:d}'.format(value))
        return True
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return False
