#!/usr/bin/python3
import sys


def main():
    sys.stdout = sys.stderr
    dora = "and that piece of art is useful - Dora Korpar, 2015-10-19"
    sys.stderr.write(dora + "\n")
    sys.exit(1)


main()
