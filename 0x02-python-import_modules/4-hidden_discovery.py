#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    o_hidden_4 = dir()
    for i in range(0, len(o_hidden_4)):
        if not o_hidden_4[i][0:2] == "__":
            print("{}".format(o_hidden_4[i]))
