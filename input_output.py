#!/usr/bin/env python3
from algo2_better_enumeration import enumeration
from algo4_linear import linear

test_arrays = []
text_output = open('test_out.txt', 'w')


def write_results(a, r):
    """A method that writes results to an output file opened with text_output.

    Arguments:
        a   -- This is the original array that needs to be printed.
        r   -- This is a tuple that contains a subarray and max sum.
    """
    text_output.write(str(a) + '\n')
    text_output.writelines(str(r[0]) + '\n')
    text_output.write(str(r[1]) + '\n\n')


# This is currently set to open the text file given to us and read each line into an array that is
# stored in test_arrays.
with open('MSS_Problems.txt', 'r') as text_input:
    for line in text_input:
        line = line.strip('[\n').replace(',', '').replace(']', '')

        if line != '' and line is not None:
            array = [int(n) for n in line.split(' ')]
            test_arrays.append(array)

# This iterates over each array that we are testing and calls the enumeration function. The results
# are then written to a file called "test_out.txt". The output file name will be changed before
# we submit, I just wanted to avoid overwriting the file that was given to us from the prof.
for array in test_arrays:
    text_output.write("Results for enumeration\n")
    results = enumeration(array)
    write_results(array, results)

    text_output.write("Results for linear\n")
    results = linear(array)
    write_results(array, results)


text_output.close()

