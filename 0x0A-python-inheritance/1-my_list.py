#!/usr/bin/python3
"""Contains definiton for the class MyList that inherits from list."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
