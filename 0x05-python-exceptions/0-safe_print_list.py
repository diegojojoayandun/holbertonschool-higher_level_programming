#!/usr/bin/python3
def safe_print_list(my_list, limit):
    counter = 0
    for i in range(0, limit):
        try:
            print("{:d}".format(my_list[i]), end="")
            counter += 1
        except IndexError:
            pass
    print()
    return counter
