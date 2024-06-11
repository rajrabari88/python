'''
When will the else part of try-except-else be executed?

'''

try:
    result = 10 / 2  
except ZeroDivisionError:
    print("Error: Division by zero!")
else:
    print("Division was successful. Result:", result)
