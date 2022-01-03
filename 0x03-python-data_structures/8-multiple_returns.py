#!/usr/bin/python3
def multiple_returns(sentence):
    _tuple = ()
    if not sentence == "":
        _tuple = len(sentence), sentence[0]
    else:
        _tuple = 0, "None"
    return _tuple
