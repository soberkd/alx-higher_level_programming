#!/usr/bin/python3

def max_integer(my_list=[]):
    length = len(my_list)
    max_value = 0
    if length == 0:
        return "None"
    if my_list:
        for value in my_list:
            if value > max_value:
                max_value = value
        return (max_value)
