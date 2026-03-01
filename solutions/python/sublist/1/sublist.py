"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def sublist(list_one, list_two):
    
    if list_one == list_two:

        return EQUAL

    if len(list_one) > len(list_two):

        index = 0

        for index in range(0, len(list_one)):

            if list_one[index: index + len(list_two)] == list_two:

                return SUPERLIST
            
    if len(list_one) < len(list_two):

        index = 0

        for index in range(0, len(list_two)):

            if list_two[index: index + len(list_one)] == list_one:

                return SUBLIST      

    return UNEQUAL