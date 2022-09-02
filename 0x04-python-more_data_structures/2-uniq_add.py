#!/usr/bin/python3

# function adds unique number of a list
def uniq_add(my_list=[]):
    num = 0
    unq_list = set(my_list)
    for i in unq_list:
        num += i
        return(num)
