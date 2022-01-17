#!/usr/bin/python3
'''Divide a list'''


def list_division(my_list_1, my_list_2, list_length):
    '''divides element by element 2 lists.'''
    result = []
    tmp = 0

    for i in range(0, list_length):
        try:
            tmp = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            tmp = 0
            print("division by 0")
        except TypeError:
            tmp = 0
            print("wrong type")
        except IndexError:
            tmp = 0
            print("out of range")
        finally:
            pass
        result.append(tmp)
    return result
