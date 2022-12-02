#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """ Prints all integers of a list, in reverse order
    Args:
        my_list: list to reverse
    """
    for x in reversed(my_list):
        print("{}".format(x))
