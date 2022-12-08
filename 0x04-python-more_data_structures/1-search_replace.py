#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map(lambda element: element if element != search else
                        replace, my_list))
    return (new_list)
