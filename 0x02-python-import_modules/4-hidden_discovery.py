#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    ls = dir(hidden_4)
    for i in ls:
        if i[:2] != "__":
            print("{:s}".format(i))
