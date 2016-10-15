#!/usr/bin/env python3
# John Blakey
# Source example: http://www.geeksforgeeks.org/divide-and-conquer-maximum-sum-subarray/

import time


start_time = time.time()

def print_array(array):
	print('[', end='')
	print(*array, sep=', ', end='')
	print(']')

# compare first element of the array
# first element of array is the calculated sum
def max_subarray(arrayA, arrayB, arrayC = None):
	if arrayC is None:
		if arrayA[0] > arrayB[0]:
			return arrayA
		else:
			return arrayB
	else:
		return max_subarray(max_subarray(arrayA, arrayB), arrayC)

def max_sum_cross_subarray(array, low, middle, high):
	# left subarray (low to middle)
	temp_sum = 0
	left_sum = 0
	max_left = 0
	for i in range(middle, -1, -1):
		temp_sum += array[i]
		if temp_sum > left_sum:
			left_sum = temp_sum
			max_left = i

	# right subarray (middle + 1 to high)
	temp_sum = 0
	right_sum = 0
	max_right = 0
	for i in range(middle + 1, high + 1):
		temp_sum += array[i]
		if temp_sum > right_sum:
			right_sum = temp_sum
			max_right = i

	# return an array result = [x, y, z]
	# x = sum, y = first element of answer subarry, z = last element of answer subarray
	return [left_sum + right_sum, max_left, max_right]

def max_sum_subarray(array, low, high):
	# one element stops execution (base case)
	if low == high:
		# return an array result = [x, y, z]
		# x = sum, y = first element of answer subarry, z = last element of answer subarray
		return [array[low], low, high]

	# calculate middle element
	middle = (low + high) // 2	# '//' denotes integer division

	# max sum in left subarray
	# max sum in right subarray
	# max sum crosses middle element
	return max_subarray(max_sum_subarray(array, low, middle), 
				max_sum_subarray(array, middle + 1, high),
				max_sum_cross_subarray(array, low, middle, high))

def max_sum_sequence(array):
	print_array(array)
	answer_array = max_sum_subarray(array, 0, len(array) - 1)
	print_array(array[answer_array[1]:answer_array[2] + 1])
	print(answer_array[0])

#Test Cases:

max_sum_sequence([4, 4, -10, 3, -2, 1])

#max_sum_sequence([-2])

max_sum_sequence([-2, -5, 6, -2, -3, 1, 5])
#answer [6, -2, -3, 1, 5] = 7

#max_sum_sequence([4, 3, -10, 3, -1, 2, 0, -3, 5, 7, -4, -8, -10, 4, 7, -30, -2, -6, 4, 7])

execution_time = time.time() - start_time
print ("\n\nexecution_time: {}".format(execution_time))