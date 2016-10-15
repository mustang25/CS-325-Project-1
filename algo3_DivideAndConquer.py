#!/usr/bin/env python3
# John Blakey

import time


start_time = time.time()

# TODO
# print original array
# L[]
# print(*L, sep=', ')

def max_sum_cross_subarray(array, low, middle, high):
	#left subarray (low to middle)
	temp_sum = 0
	left_sum = 0
	for i in range(middle, 0, -1):	# verify this is correct
		temp_sum = temp_sum + array[i]
		if temp_sum > left_sum:
			left_sum = temp_sum

	#right subarray (middle + 1 to high)
	temp_sum = 0
	right_sum = 0
	for i in range(middle + 1, high):	# verify this is correct
		temp_sum = temp_sum + array[i]
		if temp_sum > right_sum:
			right_sum = temp_sum

	return left_sum + right_sum

def max_sum_subarray(array, low, high):
	# one element stops calculation (base case)
	if low == high:
		return array[low]

	#middle element
	middle = (low + high) / 2

	# max sum in left subarray
	# max sum in right subarray
	# max sum crosses middle element
	# max function incorrect in this case
	return max(max_sum_subarray(array, low, middle), 
				max_sum_subarray(array, middle + 1, high),
				max_sum_cross_subarray(array, low, middle, high))

def max_sum_sequence(array):
	return max_sum_subarray(array, 0, len(array) - 1)
	

print (max_sum_sequence([4, 5, -10, 3]))

print (max_sum_sequence([4]))

#print (max_sum_sub_sequence([4, 3, -10, 3, -1, 2, 0, -3, 5, 7, -4, -8, -10, 4, 7, -30, -2, -6, 4, 7]))

execution_time = time.time() - start_time
print ("\n\nexecution_time: {}".format(execution_time))