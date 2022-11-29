#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) < 123:
            lower = ord(char) - 32
            upper = chr(lower)
            print("{}".format(upper), end="")
        else:
            print("{}".format(char), end="")
    print()
