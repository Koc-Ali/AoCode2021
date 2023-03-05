import os

# file handling
fileDir = os.path.dirname(os.path.realpath('__file__'))

# For accessing the file in the same folder
filename = "2021_advent_3.input.txt"
# filename = "2021_advent_3.input.sample.txt"

path_to_file = fileDir + '/' + filename

file = open(os.path.expanduser(path_to_file))

# problem solution
bin_numbers = []

# read codes in array
for line in file:
    fields = line.strip().split()
    bin_number = fields[0]
    print(bin_number)

    bin_numbers.append(bin_number)

# count digits
len_bin_number = len(bin_numbers[0])
bit_counters = [0]*len_bin_number
for number in bin_numbers:
    for i in range (len_bin_number):
        if number[i] == '1':
            bit_counters[i] += 1
print(bit_counters)

# create bin_code for gama_rate
total_codes = len(bin_numbers)
gama_rate = ''
for i in range(len_bin_number):
    if bit_counters[i] > int(total_codes/2):
        gama_rate += '1'
    else:
        gama_rate += '0'
print(gama_rate)
# convert binary string to int
gama_rate_value = int(gama_rate, 2)
print(gama_rate_value)
# calc and convert epsilon rate
epsilon_rate = ''.join(['1' if i == '0' else '0' for i in gama_rate])
epsilon_rate_value = int(epsilon_rate, 2)
print(epsilon_rate)
print(epsilon_rate_value)

# calculate power consumption
power_consumption = gama_rate_value*epsilon_rate_value
print('consumption rate =', power_consumption)
