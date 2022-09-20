#!/usr/bin/python3

def print_last_digit(number):
    lastdigit = abs(number) % 10
    print(lastdigit, end="")
    return lastdigit
