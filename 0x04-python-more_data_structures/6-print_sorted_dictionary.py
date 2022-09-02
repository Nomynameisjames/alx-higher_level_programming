#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_srt = list(a_dictionary.keys())
    list_srt.sort()
    for i in list_srt:
        print("{} {}".format(i, a_dictionary.get(i)))
