#!/usr/bin/python3

"""Print a square with the charracter #

"""


def print_square(size):
    """Print square"""
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for side in range(size):
        print('#' * size)
