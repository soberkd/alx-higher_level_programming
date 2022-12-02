#!/usr/bin/python3


def element_at(my_list, idx):
    """Retrieves an element from a list
    Args:
        my_list: list
        idx: position in list
    Returns:
        value of element
    """
    for element in my_list:
        if my_list.index(element) == idx:
            return (element)
