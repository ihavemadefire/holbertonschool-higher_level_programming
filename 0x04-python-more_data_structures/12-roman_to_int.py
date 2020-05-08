#!/usr/bin/python3
def roman_to_int(roman_string):
    roma_aeterna = 0
    if type(roman_string) is not str or len(roman_string) < 1:
        return 0
    n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r = roman_string
    for i in range(0, len(r)):
        if i < len(r) - 1 and n[r[i]] < n[r[i + 1]]:
            roma_aeterna -= n[r[i]]
        else:
            roma_aeterna += n[r[i]]
    return roma_aeterna
