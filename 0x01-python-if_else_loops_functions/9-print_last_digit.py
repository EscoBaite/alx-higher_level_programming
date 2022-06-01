#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        l_num = number % 10
    else:
        l_num = number % -10
        l_num *= -1

    print("{:d}".format(l_num), end='')
    return (l_num)
