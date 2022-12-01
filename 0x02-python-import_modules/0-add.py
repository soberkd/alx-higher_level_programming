#!/usr/bin/python3

from add_0 import add


def print_add():
    a = 1
    b = 2
    total = add(a, b)
    print("{} + {} = {}".format(a, b, total))


print_add()
