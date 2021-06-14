#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: June 14, 2021
# This program generates 10 random numbers into an array/list between 0 and
# 100 and displays the number with the lowest value

import constants
import random


def find_min_value(array):
    # checks for the lowest value/number in a list
    min = constants.MAX_NUM + 1

    for number in array:
        if (number < min):
            min = number
    return min


def main():
    # create an empty list
    number_array = []

    for counter in range(constants.MAX_ARRAY_SIZE):
        # generate random number from 0 to 100 and add it to the list
        random_number = random.randint(constants.MIN_NUM, constants.MAX_NUM)
        number_array.append(random_number)

        # display the random number added and at which position/index
        print("{0} added to the list at position {1}.\
". format(random_number, counter))
    print()

    # call function to check for the lowest value in the list
    min_value = find_min_value(number_array)

    # display the lowest value in the list
    print("The minimum value is: {}". format(min_value))
    print()


if __name__ == "__main__":
    main()
