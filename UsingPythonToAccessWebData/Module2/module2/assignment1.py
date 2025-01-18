# 
import re

# Open the file
with open('regex_sum_2157095.txt', 'r') as file:
    data = file.read()

# Use re.findall() to find all occurrences of numbers (integers)
numbers = re.findall('[0-9]+', data)

# Convert the extracted strings to integers and calculate the sum
sum_of_numbers = sum([int(number) for number in numbers])

# Print the sum
print(sum_of_numbers)