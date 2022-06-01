#!/usr/bin/python3
for letter in range(26):
    if letter != 4 and letter != 16:
        print("{:s}".format(chr(letter + ord("a"))), end="")