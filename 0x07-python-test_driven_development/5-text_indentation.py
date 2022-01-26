#!/usr/bin/python3
"""Module text_indentation
"""

def text_indentation(text):
    """text_indentation - prints a text with 2 new lines after of : ., ? and :
    Arguments: text must be a string.
    Return:Nothing"""

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] == " ":
            j = i - 1
            if text[j] != "." and text[j] != "?" and text[j] != ":" and \
               text[j] != " ":
                print("{}".format(text[i]), end="")
        else:
            print("{}".format(text[i]), end="")
            if text[i] == "." or text[i] == "?" or text[i] == ":":
                print('\n')
