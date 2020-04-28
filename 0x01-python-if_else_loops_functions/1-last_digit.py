#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = abs(number)
a = a % 10
if number < 0:
    b = -a
else:
    b = a
if a == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, b))
if a > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, b))
else:
    print("Last digit of {:d} is {:d} ".format(number, b), end="")
    print("and is less than 6 and not 0")
