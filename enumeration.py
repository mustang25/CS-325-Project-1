#!/usr/bin/env python3


def enumeration(array):
    max_sum = array[0]
    start_index = 0
    end_index = 1

    for i, first_value in enumerate(array):
        for j, next_value in enumerate(array, i+1):
            current_sum = 0
            for value in array[i:j+1]:
                current_sum += value
            if current_sum > max_sum:
                max_sum = current_sum
                start_index = i
                end_index = j+1

    return array[start_index:end_index], max_sum


def better_enumeration(array):
    max_sum = array[0]
    start_index = 0
    end_index = 1

    for i, first_value in enumerate(array):
        current_sum = first_value

        for j, next_value in enumerate(array[i + 1:], i + 1):
            current_sum += next_value

            if current_sum > max_sum:
                max_sum = current_sum
                start_index = i
                end_index = j + 1

        if current_sum > max_sum:
            max_sum = current_sum
            start_index = i
            end_index = j + 1

    return array[start_index:end_index], max_sum


if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    return_vals = better_enumeration(arr)

    print("{}\n{}\n{}".format(arr, return_vals[0], return_vals[1]))


