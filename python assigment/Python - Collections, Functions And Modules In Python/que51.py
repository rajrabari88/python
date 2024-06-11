'''
• Write a Python function to check whether a number is perfect or not.
'''
def perfect_number(number):
    divisor_sum = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            divisor_sum += i
    return divisor_sum == number
print(perfect_number(6))   
print(perfect_number(28))  
print(perfect_number(12))  
