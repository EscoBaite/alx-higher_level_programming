#!/usr/bin/python3
""" Define a square class """


class Square:
    """ Represents a Square """

    def __init__(self, size):
        """ Initialises new Square
        Args:
            size (int): size of side of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ returns current area of the square """
        return (self.__size * self.__size)
