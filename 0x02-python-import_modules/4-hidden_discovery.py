#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for each in names:
        if each[:2] != "__":
            print("{}".format(each))
