#!/usr/bin/env python3


def enumeration(array):
    max_sum = 0
    start_index = 0
    end_index = 1

    for i, first_value in enumerate(array):
        current_sum = first_value

        for j, next_value in enumerate(array[i+1:], i + 1):
            current_sum += next_value

            if current_sum > max_sum:
                max_sum = current_sum
                start_index = i
                end_index = j + 1

    return array[start_index:end_index], max_sum


if __name__ == '__main__':
    arr = [10, -11, -1, -9, 33, -45, 23, 24, -1, -7 -8, 19]
    return_vals = enumeration(arr)

    print("{}\n{}\n{}".format(arr, return_vals[0], return_vals[1]))


