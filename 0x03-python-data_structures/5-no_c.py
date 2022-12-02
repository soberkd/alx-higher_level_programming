#!/usr/bin/python3

def no_c(my_string):
    """ removes all characters c and C from a string
    Args:
        my_string: string to remove c and C
    Returns:
        the new string
    """
    new_string = ''
    for strn in my_string:
        if strn != 'c' and strn != 'C':
            new_string += strn
    return (new_string)
