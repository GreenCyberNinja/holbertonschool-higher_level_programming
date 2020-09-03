#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    al = len(sys.argv)
    print("{:d} argument".format(al - 1), end='')
    if al == 1:
        print("s.")
    elif al == 2:
        print(":")
    else:
        print("s:")
    if al > 1:
        for i in range(al):
            if i != 0:
                print("{:d}: {:s}".format(i, sys.argv[i]))
