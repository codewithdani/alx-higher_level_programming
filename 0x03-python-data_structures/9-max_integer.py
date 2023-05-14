#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]
    for x in range(0, len(my_list)):
        if int(my_list[x] > int(max)):
            max = my_list[x]
    return max
