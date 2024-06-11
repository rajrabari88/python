'''
Write a Python program to find the maximum and minimum numbers
from the specified decimal numbers
'''
def find_max_min_decimal(numbers):
    max_number = max(numbers)
    min_number = min(numbers)    
    return max_number, min_number
decimal_numbers = [3.14, 2.71, 1.618, 0.577, 2.71828]
max_number, min_number = find_max_min_decimal(decimal_numbers)

print("Maximum number:", max_number)
print("Minimum number:", min_number)
