#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_of_a = len(tuple_a)
    len_of_b = len(tuple_b)

    if len_of_a == 0:
        i1 = 0
        i2 = 0
    elif len_of_a == 1:
        i1 = tuple_a[0]
        i2 = 0
    else:
        i1 = tuple_a[0]
        i2 = tuple_a[1]

    if len_of_b == 0:
        j1 = 0
        j2 = 0
    elif len_of_b == 1:
        j1 = tuple_b[0]
        j2 = 0
    else:
        j1 = tuple_b[0]
        j2 = tuple_b[1]

    new_tuple = ((i1 + j1), (i2 + j2))
    return new_tuple
