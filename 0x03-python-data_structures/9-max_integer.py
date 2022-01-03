#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        _max = 0
        for i in my_list:
            if i >= _max:
                _max = i
        return _max
