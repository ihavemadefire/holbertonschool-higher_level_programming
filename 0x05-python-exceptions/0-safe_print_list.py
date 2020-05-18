#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(0, x):
            count += 1
            print("{}".format(my_list[i]), end='')
    except IndexError:
            count = i
    print()
    return count
