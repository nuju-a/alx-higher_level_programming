#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    sum = 0
    arg_count = len(sys.argv)

    for i in range(1, arg_count):
        sum += int(sys.argv[i])

    print("{:d}".format(sum))
