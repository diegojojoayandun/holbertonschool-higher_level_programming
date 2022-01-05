#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0

    suma = 0
    new_str=""

    _dict = {ord('I'): '1', ord('V'): '5', ord('X'): '10',\
    ord('L'): '50', ord('C'): '100', ord('D'): '500', ord('M'): 1000}
    translation = roman_string.maketrans(_dict)

    for c in roman_string:
        new_str+=c + ","

    new_str= new_str.translate(translation)
    new_str=new_str.split(",")

    for i in new_str:
        if (i != ''):
            suma += int(i)
    return suma
