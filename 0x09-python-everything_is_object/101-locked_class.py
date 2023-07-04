#!/usr/bin/python3
# 101-locked_class.py
# Eyram Cobblah
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything except an attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
