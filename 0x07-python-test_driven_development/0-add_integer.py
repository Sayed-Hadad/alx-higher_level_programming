#!/usr/bin/python3
'''
Adding integers module.
This module contains 1 function (add_integer)
'''


def add_integer(a, b=98):
    '''
    A function that adds 2 integers.
    If the arguments are floats they will be casted to integers.
    If the arguments aren't of type int, or float, it raises a TypeError
    '''

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError('a must be an integer')
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return (a + b)
