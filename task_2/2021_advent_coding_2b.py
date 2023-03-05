import os

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

# For accessing the file in the same folder
filename = "2021_advent_2.input.txt"
# filename = "2021_advent_2.input.sample.txt"

path_to_file = fileDir + '/' + filename

file = open(os.path.expanduser(path_to_file))

# problem solution
horizontal_pos = 0
depth_pos = 0
aim = 0

for line in file:
    fields = line.strip().split()
    steps = int(fields[1])

    if fields[0] == "forward":
        horizontal_pos += steps
        depth_pos += aim*steps
    if fields[0] == "down":
        aim += steps
    if fields[0] == "up":
        aim -= steps


print('total hor pos =', horizontal_pos, 'total_dep_pos = ', depth_pos, 'score = ', horizontal_pos*depth_pos)

