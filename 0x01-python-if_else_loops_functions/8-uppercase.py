#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            nueva = chr(ord(c) - 32)
        else:
            nueva = c
        print("{:s}".format(nueva), end="")
    print('')
