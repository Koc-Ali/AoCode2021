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

for line in file:
    fields = line.strip().split()
    current_depth = int(fields[0])

    height_values.append(current_depth)

for i in range(len(height_values)):
    if i+3 < len((height_values)):
        Sum1 = height_values[i]+height_values[i+1]+height_values[i+2]
        Sum2 = height_values[i+1]+height_values[i+2]+height_values[i+3]

        if Sum2 > Sum1:
            amount_of_increases += 1

print(amount_of_increases)
