#!/usr/bin/python3
"""Defines a function that print squares."""

def print_square(size):
    """Function that prints a square of a size supplied as a argument when calling the method

    Args:
        size: ize of the square to be printed

        Returns:
            No return value 

        Raises:
            TypeError: if size is not an integer
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)


