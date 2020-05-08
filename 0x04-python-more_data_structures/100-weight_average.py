#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) < 1 or my_list is None:
        return 0
    weight = num = 0
    for i in my_list:
        weight += i[1]
    for i in my_list:
        num += (i[0] * i[1])
    average = num / weight
    return average
