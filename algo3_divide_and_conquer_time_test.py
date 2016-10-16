#!/usr/bin/env python3
# John Blakey
# Source example: http://www.geeksforgeeks.org/divide-and-conquer-maximum-sum-subarray/

import time
import random

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
	max_left = middle - 1
	for i in range(middle, -1, -1):
		temp_sum += array[i]
		if temp_sum > left_sum:
			left_sum = temp_sum
			max_left = i

	# right subarray (middle + 1 to high)
	temp_sum = 0
	right_sum = 0
	max_right = middle
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

def divide_and_conquer(array):
	start_time = time.time()

	answer_array = max_sum_subarray(array, 0, len(array) - 1)

	execution_time = time.time() - start_time
	print ("\n\nexecution_time: {}".format(execution_time))

	print_array(array)
	print_array(array[answer_array[1]:answer_array[2] + 1])
	print(answer_array[0])

	return execution_time

#main
array_size = int(input('Input integer for the size of an array to test the algorithm: '))

iterations = 10
total_time = 0

for i in range(0, iterations):
	test_array = [None] * array_size
	for j in range(0, array_size):
		test_array[j] = random.randint(-100, 100)

	total_time += divide_and_conquer(test_array)

print('Average time =', total_time / iterations, "\nn =", array_size)

#output information to text file
text_output = open('algo3_time_results', 'a')

# copy 'n tab average_time(seconds) on the first line'
text_output.write(str(array_size))
text_output.write(str("\t"))
text_output.write(str(total_time / iterations))

text_output.close()

#n = 100, 200,...,900 or 1000,2000,...,10000
# 10 different input arrays for each