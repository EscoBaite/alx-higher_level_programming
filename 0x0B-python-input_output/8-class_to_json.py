#!/usr/bin/python3
"""Defines a function that returns the dictionary description."""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
    return obj.__dict__
