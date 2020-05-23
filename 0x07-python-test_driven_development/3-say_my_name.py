#!/usr/bin/python3
"""This module defines a funtion say_my_name"""


def say_my_name(first_name, last_name=""):
    """Defines a funtion say_my_name """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    if first_name is None:
        raise NameError('name \'{:s}\' is not defined'.format(first_name))
    if last_name is None:
        raise NameError('name \'{:s}\' is not defined'.format(last_name))

    print("My name is {:s} {:s}".format(first_name, last_name))
