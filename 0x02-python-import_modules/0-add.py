#!/usr/bin/python3
from add_0 import add


def addvars():
    # Assigns variables #
    a = 1
    b = 2
    # prints the addition of the variables #
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))


if __name__ == "__main__":
    addvars()
