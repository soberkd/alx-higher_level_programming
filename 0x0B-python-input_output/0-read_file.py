#!/usr/bin/python3
"""Module that reads a file"""


def read_file(filename=""):
    """Read file"""
    with open(filename, mode='r', encoding='UTF-8') as read_file:
        for line in read_file:
            print(line, end="")
