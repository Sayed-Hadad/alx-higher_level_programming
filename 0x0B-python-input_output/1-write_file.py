#!/usr/bin/python3
"""
This module is part of Alx python tasks.
It contains one function, write_file(),
which write a text to a file
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8),
    and returns the number of characters written,
    It creates the file if doesn’t exist, and overwrites
    the content of the file if it already exists.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
