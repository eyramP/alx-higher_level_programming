#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_keys = list(a_dictionary.keys())
    dict_keys.sort()
    for key in dict_keys:
        print("{} : {}".format(key, a_dictionary.get(key)))
