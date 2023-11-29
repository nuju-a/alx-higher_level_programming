#!/usr/bin/python3


def uppercase(str):
    upper = ''
    for char in str:
        if (ord('a') <= ord(char) <= ord('z')):
            char = chr(ord(char) - 32)
        upper += char
    print(upper)
