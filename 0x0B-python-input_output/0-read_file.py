#!/usr/bin/python3
"""
This module is a part of Alx python tasks.
It contains a function for reading text files in UTF-8,
and printing it to stdout
"""


def read_file(filename=""):
    """
    a function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
