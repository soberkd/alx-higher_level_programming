#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if my_list:
        for item in my_list:
            if my_list.index(item) == idx:
                del my_list[idx]
        return (my_list)
