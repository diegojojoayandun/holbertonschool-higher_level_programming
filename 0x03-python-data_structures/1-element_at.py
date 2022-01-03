#!/usr/bin/pithon3
def element_at(my_list, idx):
    if not idx < 0 and not idx > len(my_list) - 1:
        return my_list[idx]
    else:
        return 'None'
