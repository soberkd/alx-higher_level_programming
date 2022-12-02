#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """ Replaces an element of a list at a specific position without
    modifying the original list
    Args:
        my_list: list
        idx: position to replace an element
        element: new to replace
    Returns:
        New list with repleced value or
        old list if @idx out range
    """
    if idx > (len(my_list) - 1) or idx < 0:
        return (my_list)
    for x in my_list:
        if my_list.index(x) == idx:
            new_list = my_list.copy()
            new_list[idx] = element
    return (new_list)
