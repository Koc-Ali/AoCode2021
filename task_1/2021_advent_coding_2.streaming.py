# solution with stream handling...

import os

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

# For accessing the file in the same folder
filename = "2021_advent_1.input.txt"
#filename = "2021_advent_3.input.sample.txt"

# filename = "2022_advent_10.input.sample.txt"
# filename = "2022_advent_10.input.sample2.txt"

path_to_file = fileDir + '/' + filename

file = open(os.path.expanduser(path_to_file))

# problem solution
amount_of_increases = 0

height_values = []
H1_1 = 0
H1_2 = 0
H1_3 = 0
H2_1 = 0
H2_2 = 0
H2_3 = 0

read_first_4_values = 0

for line in file:
    fields = line.strip().split()
    current_depth = int(fields[0])

    if read_first_4_values in range (4):
        if read_first_4_values == 0:
            H1_1 = current_depth
            read_first_4_values += 1
        elif read_first_4_values == 1:
            H1_2 = current_depth
            H2_1 = current_depth
            read_first_4_values += 1
        elif read_first_4_values == 2:
            H1_3 = current_depth
            H2_2 = current_depth
            read_first_4_values += 1
        elif read_first_4_values == 3:
            H2_3 = current_depth
            read_first_4_values += 1
        sum1 = H1_1+H1_2+H1_3
        sum2 = H2_1+H2_2+H2_3
        if sum2 > sum1:
            amount_of_increases += 1
    else:
        H1_1 = H2_1
        H1_2 = H2_2
        H1_3 = H2_3
        H2_1 = H2_2
        H2_2 = H2_3
        H2_3 = current_depth
        sum1 = H1_1+H1_2+H1_3
        sum2 = H2_1+H2_2+H2_3
        if sum2 > sum1:
            amount_of_increases += 1

print(amount_of_increases)
