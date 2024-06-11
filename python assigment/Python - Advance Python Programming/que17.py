'''
 When is the finally block executed?

 '''

try:
    result = 10 / 2 
except ZeroDivisionError:
    print("Error: Division by zero!")
finally:
    print("Finally block executed.")
