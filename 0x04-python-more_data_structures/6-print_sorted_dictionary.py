#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    [print("{:s} : {}".format(key, value)) for key, value in
     sorted(a_dictionary.items())]
