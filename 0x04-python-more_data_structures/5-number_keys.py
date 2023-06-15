#!/usr/bin/python3
def number_keys(a_dictionary):
    sum = 0

    d_keys = list(a_dictionary.keys())
    for key in d_keys:
        sum += 1

    return sum
