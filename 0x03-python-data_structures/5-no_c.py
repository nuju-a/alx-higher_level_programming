#!/usr/bin/python3


def no_c(my_string):
    empty_string = ''
    for i in my_string:
        if i != 'c' and  i != 'C':
            empty_string += i
    return empty_string
