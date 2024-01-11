#!/usr/bin/python3
"""
say_my_name module, it contains one function, which is
say_my_name(), it prints My name is <first_name> last_name
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name() a function that prints the full name
    passed to it, if the areguments aren't strings, then
    it raises an TypeError message
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print(f'My name is {first_name} {last_name}')
