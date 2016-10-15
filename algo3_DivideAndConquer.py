#!/usr/bin/env python3
# John Blakey
# Source example: http://www.geeksforgeeks.org/divide-and-conquer-maximum-sum-subarray/

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
	for i in range(middle, -1, -1):
		temp_sum = temp_sum + array[i]
		if temp_sum > left_sum:
			left_sum = temp_sum

	#right subarray (middle + 1 to high)
	temp_sum = 0
	right_sum = 0
	for i in range(middle + 1, high + 1):
		temp_sum = temp_sum + array[i]
		if temp_sum > right_sum:
			right_sum = temp_sum

	return left_sum + right_sum

def max_sum_subarray(array, low, high):
	# one element stops execution (base case)
	if low == high:
		return array[low]

	#calculate middle element
	middle = (low + high) // 2	# '//' denotes integer division

	# max sum in left subarray
	# max sum in right subarray
	# max sum crosses middle element
	return max(max_sum_subarray(array, low, middle), 
				max_sum_subarray(array, middle + 1, high),
				max_sum_cross_subarray(array, low, middle, high))

def max_sum_sequence(array):
	return max_sum_subarray(array, 0, len(array) - 1)
	

#print (max_sum_sequence([4, 3, -10, 3, -1, 5]))

#print (max_sum_sequence([-2]))

print (max_sum_sequence([-2, -5, 6, -2, -3, 1, 5, -6]))

print (max_sum_sequence([4, 3, -10, 3, -1, 2, 0, -3, 5, 7, -4, -8, -10, 4, 7, -30, -2, -6, 4, 7]))

execution_time = time.time() - start_time
print ("\n\nexecution_time: {}".format(execution_time))