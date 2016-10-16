#!/usr/bin/env python3

import random
import time
from algo2_better_enumeration import enumeration, better_enumeration
from algo3_divide_and_conquer_time_test import divide_and_conquer
from algo4_linear import linear

text_output = open('timing.txt', 'w')

# Algorithm 1 testing.
total_time = 0
n = [100, 200, 300, 350, 400, 450, 500, 550, 600, 650]
text_output.write("Enumeration Results:\n")
text_output.write("Array Size\tRunning Time\n")
for size in n:
    total_time = 0
    for _ in range(10):
        test_array = [random.randrange(-100, 100) for i in range(size)]
        start_time = time.time()
        enumeration(test_array)
        execution_time = time.time() - start_time
        total_time += execution_time

    average = total_time/10

    text_output.write("{}\t\t\t{}\n".format(size, average))

# Algorithm 2 testing
total_time = 0
n = [100, 200, 300, 400, 500, 1000, 2000, 4000, 8000, 10000]
text_output.write("\nBetter Enumeration Results:\n")
text_output.write("Array Size\tRunning Time\n")
for size in n:
    total_time = 0
    for _ in range(10):
        test_array = [random.randrange(-100, 100) for i in range(size)]
        start_time = time.time()
        better_enumeration(test_array)
        execution_time = time.time() - start_time
        total_time += execution_time

    average = total_time/10

    text_output.write("{}\t\t\t{}\n".format(size, average))

# Algorithm 3 testing
text_output.write("\nDivide & Conquer Results:\n")
text_output.write("Array Size\tRunning Time\n")
for size in n:
    total_time = 0
    for _ in range(10):
        test_array = [random.randrange(-100, 100) for i in range(size)]
        total_time += divide_and_conquer(test_array)

    average = total_time/10

    text_output.write("{}\t\t\t{}\n".format(size, average))


# Algorithm 4 testing
n = [1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000, 512000]
text_output.write("\nLinear Results:\n")
text_output.write("Array Size\tRunning Time\n")
for size in n:
    total_time = 0
    for _ in range(10):
        test_array = [random.randrange(-100, 100) for i in range(size)]
        start_time = time.time()
        linear(test_array)
        execution_time = time.time() - start_time
        total_time += execution_time

    average = total_time/10

    text_output.write("{}\t\t\t{}\n".format(size, average))

text_output.close()
