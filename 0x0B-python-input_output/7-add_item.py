#!/usr/bin/python3
"""Module adds arguments to a list and saves to file"""


from sys import argv


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_\
        json_file

    filename = "add_item.json"

    try:
        python_list = load_from_json_file(filename)
    except FileNotFoundError:
        python_list = []

    for arg in argv:
        if arg != argv[0]:
            python_list.append(arg)

    save_to_json_file(python_list, filename)
