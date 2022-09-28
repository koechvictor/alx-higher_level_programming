#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list or my_list is None:
        return 0
    totalV = 0
    weight = 0
    for i in my_list:
        totalV += i[0] * i[1]
        weight += i[1]
    return totalV / weight
