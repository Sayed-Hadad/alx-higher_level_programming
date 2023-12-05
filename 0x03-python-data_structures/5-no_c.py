#!/usr/bin/python3
def no_c(my_string):
    no_c = ""
    for letter in my_string:
        if letter not in "Cc":
            no_c += letter
    return no_c
