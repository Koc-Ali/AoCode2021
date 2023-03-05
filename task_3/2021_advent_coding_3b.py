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

def read_numbers(numbers):
    # read codes in array
    for line in file:
        fields = line.strip().split()
        bin_number = fields[0]
        print(bin_number)

        numbers.append(bin_number)
    return numbers

bin_numbers = read_numbers(bin_numbers)
len_bin_number = len(bin_numbers[0])

def determine_most_common_bit(numbers, position):
    # count digits
    bit_count = 0
    for number in numbers:
        if number[position] == '1':
            bit_count += 1
    amount_numbers = len(numbers)
    equal = False
    if (bit_count == amount_numbers//2) and (amount_numbers%2 == 0):
        equal = True
    if bit_count > int(amount_numbers/2):
        return('1', equal)
    else:
        return('0', equal)
def determine_least_common_bit(numbers, position):
    # count digits
    bit_count = 0
    for number in numbers:
        if number[position] == '1':
            bit_count += 1
    amount_numbers = len(numbers)
    equal = False
    if (bit_count == amount_numbers//2) and (amount_numbers%2 == 0):
        equal = True
    if bit_count > int(amount_numbers/2):
        return('0', equal)
    else:
        return('1', equal)
def determine_sub_numbers(numbers, position, bit):
    matching_list = []
    for number in numbers:
        if number[position] == bit:
            matching_list.append(number)
    return matching_list

def find_oxygen_rate(numbers):
    bit_position = 0
    num_digits = len(numbers[0])
    while (len(numbers) > 1) and (bit_position < num_digits):
        most_common_bit, equal = determine_most_common_bit(numbers, bit_position)
        if equal:
            numbers = determine_sub_numbers(numbers, bit_position, '1')
        else:
            numbers = determine_sub_numbers(numbers, bit_position, most_common_bit)
        bit_position += 1
    if len(numbers) == 1:
        return numbers[0]

def find_Co2_rate(numbers):
    bit_position = 0
    num_digits = len(numbers[0])
    while (len(numbers) > 1) and (bit_position < num_digits):
        least_common_bit, equal = determine_least_common_bit(numbers, bit_position)
        if equal:
            numbers = determine_sub_numbers(numbers, bit_position, '0')
        else:
            numbers = determine_sub_numbers(numbers, bit_position, least_common_bit)
        bit_position += 1
    if len(numbers) == 1:
        return numbers[0]

oxygen_bin_value = find_oxygen_rate(bin_numbers)
oxygen_value = int(oxygen_bin_value, 2)

print('oxygen_rate = ', oxygen_bin_value, 'oxygen value =', oxygen_value)

Co2_bin_value = find_Co2_rate(bin_numbers)
Co2_value = int(Co2_bin_value, 2)

print('Co2_rate = ', Co2_bin_value, 'Co2 value =', Co2_value)

life_support_rating = oxygen_value * Co2_value

print('life support rating  = ', life_support_rating)







