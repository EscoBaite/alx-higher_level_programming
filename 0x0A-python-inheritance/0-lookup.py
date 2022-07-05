#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of an object's available attributes.
     Args:
        obj (any): object whose attributes and methods are to be returned
    """
    return (dir(obj))
