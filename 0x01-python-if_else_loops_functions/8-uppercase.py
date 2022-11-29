#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) < 123:
            lower = ord(char) - 32
            char = chr(lower)
        print("{}".format(char), end="")
    print()
