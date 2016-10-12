#!/usr/bin/env python3
# Calculate the running time of a program
# Created by John Blakey
# From Question 7 of HW1

#Python module used to time execution
import time

# Example function to test running time
def fibRec(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibRec(n - 1) + fibRec(n - 2)

# Ask for input
userIn = int(input('Input the number of Fibonacci numbers to calculate:'))

# start clock
start = time.clock()

# run example function to time its execution
print(fibRec(userIn))

# end clock
end = time.clock()

# print clock results
print(end - start)