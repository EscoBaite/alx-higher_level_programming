#!/usr/bin/python3
"""Defines a function that appends a string at the end of a text file
 and returns the number of characters added: 
"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return json.dumps(my_obj)
