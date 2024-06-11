'''
• How many except statements can a try-except block have? Name Some 
built-in exception classes:
'''


try:   
    result = 10 / 0 
except ZeroDivisionError:    
    print("Error: Division by zero!")
except ValueError:
    print("Error: Invalid value!")
except Exception as e:
    print("An error occurred:", e)
