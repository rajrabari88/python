'''
• Write a Python program to get the Factorial number of given number.
'''

def f_number(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


number = int(input("Enter a number: "))


print("Factorial (number):", f_number(number))
