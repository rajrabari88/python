'''
How will you set the starting value in generating random numbers?
'''

import random

random.seed(42)
random_number1 = random.random()
random_number2 = random.randint(1, 100)

print("Random number 1:", random_number1)
print("Random number 2:", random_number2)
