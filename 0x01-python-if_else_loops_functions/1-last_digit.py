#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10

if number < 0:
    lastdigit *= -1

print("Last digit of {:d} is ".format(number), end='')

if lastdigit == 0:
    print("{:d} and is 0".format(lastdigit))

elif lastdigit > 5:
        print("{:d} and is greater than 5".format(lastdigit))

else:
    print("{:d} and is less than 6 and not 0".format(lastdigit))
