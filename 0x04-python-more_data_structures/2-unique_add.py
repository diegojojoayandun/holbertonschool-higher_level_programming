#!/usr/bin/python3
def uniq_add(my_list=[]):
    suma = 0
    new = []
    [new.append(n) for n in my_list if n not in new]
    for i in range(len(new)):
        suma += new[i]
    return suma
