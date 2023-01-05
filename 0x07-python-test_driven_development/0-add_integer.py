#!/usr/bin/python3

""""A module that adds two numbers

This module performs the addition operation on two numbers,
these numbers can be integers of floats,
if the numbers are floats they are converted ti integers.

"""


def add_integer(a, b=98):
    """Add two numbers"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return (a + b)
