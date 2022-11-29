#!/usr/bin/python3

for alph in range(97,122):
    char = chr(alph)
    if char == 'q' or char == 'e':
        continue
    print("{}".format(char), end="")
