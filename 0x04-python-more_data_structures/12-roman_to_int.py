#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0
    rom_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    last_num = 0
    roman = roman_string[::-1]
    for letter in roman:
        current = rom_int[letter]
        if last_num > current:
            num -= current
        else:
            num += current
        last_num = current
    return num
