'''
• Explain Exception handling? What is an Error in Python?
'''
try:
    result = 10 / 0 
except ZeroDivisionError:
    print("Error: Division by zero!")
else:
    print("Result:", result)
finally:
    print("This code is always executed.")
