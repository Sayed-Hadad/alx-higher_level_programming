#!/usr/bin/python3
"""
print_square module, it contains one function, which is
print_square(), give the size of the square it prints it
using the '#' character
"""


def print_square(size):
    """
    print_square: given the size as an argument, it prints a
    square using the '#' character, if size isn't an integer
    a TypeError is raised, and if size is < 0, a ValueError is
    raised
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print('#' * size)
