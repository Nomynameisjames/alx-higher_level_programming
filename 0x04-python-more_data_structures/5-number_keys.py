#!/usr/bin/python3
# function returns number of keys in a dictionary

def number_keys(a_dictionary):
    list_keys = list(a_dictionary.keys())
    num = 0
    for i in list_keys:
        num += i
        return (num)
