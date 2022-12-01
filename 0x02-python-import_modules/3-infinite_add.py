#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    total = 0
    length = len(sys.argv) - 1
    for x in range(length):
        total += int(sys.argv[x + 1])
    print("{}".format(total))
