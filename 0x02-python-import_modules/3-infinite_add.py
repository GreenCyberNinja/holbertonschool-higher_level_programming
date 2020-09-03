#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    al = len(sys.argv)
    summy = 0
    for i in range(al):
        if i != 0:
            summy += int(sys.argv[i])
    print(int(summy))
