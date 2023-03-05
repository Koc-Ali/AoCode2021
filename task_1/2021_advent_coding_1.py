import os

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

# For accessing the file in the same folder
filename = "2021_advent_1.input.txt"
# filename = "2021_advent_3.input.sample.txt"

# filename = "2022_advent_10.input.sample.txt"
# filename = "2022_advent_10.input.sample2.txt"

path_to_file = fileDir + '/' + filename

file = open(os.path.expanduser(path_to_file))

# problem solution
last_depth = 0
amount_of_increases = -1

for line in file:
    fields = line.strip().split()
    current_depth = int(fields[0])

    if current_depth > last_depth:
        amount_of_increases += 1
    last_depth = current_depth

print(amount_of_increases)
