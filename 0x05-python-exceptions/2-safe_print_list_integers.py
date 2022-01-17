#!/usr/bin/python3
'''Print and count integers'''


def safe_print_list_integers(my_list=[], x=0):
    '''prints the first x elements of a list and only integers'''
    counter = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            counter += 1
        except (TypeError, ValueError):
            pass
    print()
    return counter
