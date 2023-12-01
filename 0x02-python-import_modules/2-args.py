#!/usr/bin/python3

if __name__ == "__main__":
    import sys

arg_count = len(sys.argv) - 1
arg_string = "argument" if arg_count == 1 else "arguments"
arg_delim = "." if arg_count == 0 else ":"

print("{} {}{}".format(arg_count, arg_string, arg_delim))

for i in range(1, arg_count + 1):
    print("{}: {}".format(i, sys.argv[i]))
