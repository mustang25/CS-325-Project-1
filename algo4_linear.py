#!/usr/bin/env python3

"""Linear algorithm based on the psuedocode from https://atekihcan.github.io/CLRS/E04.01-05/"""


def linear(array):
    """Linear algorithm to determine the maximum subarray in an array.

    The algorithm will return a subarray and the maximum sum that was found.
    Arguments:
        array   -- An array that contains at least one element.
    """
    low = 0
    high = 0
    max_sum = array[low]
    temp_sum = 0
    temp_low = 0

    for i, value in enumerate(array):
        temp_sum = max(value, temp_sum + value)
        if temp_sum == value:
            temp_low = i
        if temp_sum > max_sum:
            max_sum = temp_sum
            high = i
            low = temp_low

    return array[low:high+1], max_sum


