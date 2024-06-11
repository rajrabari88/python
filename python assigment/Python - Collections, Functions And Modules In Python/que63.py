'''
• Write a Python program to returns sum of all divisors of a number
'''
def sum_of_divisors(number):  
    divisor_sum = 0    
    for i in range(1, number + 1):
        if number % i == 0:
            divisor_sum += i   
    return divisor_sum
number = 10
print("Sum of divisors of", number, "is", sum_of_divisors(number))
