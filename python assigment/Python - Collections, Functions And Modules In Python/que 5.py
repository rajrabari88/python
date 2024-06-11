'''
Write python program that swap two number with temp variable and 
without temp variable.
'''


a = 5
b = 10
print(f"Before swapping with temp variable: a = {a}, b = {b}")
temp = a
a = b
b = temp
print(f"After swapping with temp variable: a = {a}, b = {b}")

a = 5
b = 10
print(f"Before swapping without temp variable: a = {a}, b = {b}")
a, b = b, a
print(f"After swapping without temp variable: a = {a}, b = {b}")
