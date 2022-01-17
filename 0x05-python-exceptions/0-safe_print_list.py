#!/usr/bin/python3
'''This script prints elements of a list to show the use of exceptions'''
def safe_print_list(my_list, limit):
    '''prints x elements of a list return count'''

    count = 0
    for i in range(0, limit):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            pass
    print()
    return count
