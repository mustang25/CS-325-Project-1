#!/usr/bin/env python3
from enumeration import enumeration

test_arrays = []
text_output = open('test_out.txt', 'w')

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
    text_output.write("Results for basic enumeration\n")
    results = enumeration(array)

    text_output.write(str(array) + '\n')
    text_output.writelines(str(results[0]) + '\n')
    text_output.write(str(results[1]) + '\n\n')

text_output.close()

