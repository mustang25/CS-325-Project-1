import time



start_time = time.time()



def max_sum_sub_sequence(integers):
	length = len(integers)
	list_of_sums = []

	index_of_last_summed = length

	for inty in integers:

		sum = 0
		for i in range(index_of_last_summed):
			sum += int(integers[i])

		list_of_sums.append(sum)
		index_of_last_summed -= 1

	return max(list_of_sums)

		


print max_sum_sub_sequence([4, 3, -10, 3, -1, 2, 0, -3, 5, 7, -4, -8, -10, 4, 7, -30, -2, -6, 4, 7])


execution_time = time.time() - start_time
print "\n\nexecution_time: {}".format(execution_time)