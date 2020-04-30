#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
# define vars #
a = 10
b = 5
# print funcs #
print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
