#!/usr/bin/python3
"""This module contains a single function"""


def read_lines(filename="", nb_lines=0):
    """This file reads a file for a certain number of lines"""
    lines = number_of_lines(filename)
    if nb_lines <= 0 or nb_lines > lines:
        nb_lines = lines
    with open(filename) as file:
        for i in range(nb_lines):
            print(file.readline(), end='')


def number_of_lines(filename=""):
    """This file returns a count of lines in a file"""
    count = 0
    with open(filename) as file:
        for line in file:
            count += 1
    return count
