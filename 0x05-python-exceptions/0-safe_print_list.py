#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for ech in range(0, x):
        try:
            print(my_list[ech], end="")
            count += 1
        except:
            break
    print('')
    return count


