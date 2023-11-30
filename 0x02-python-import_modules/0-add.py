#!/usr/bin/python3

"""importing the def add function to this file
this module is imported as a script so i have to set name to main
"""
if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2

    print("{} + {} = {}".format(a, b, add(a, b)))
