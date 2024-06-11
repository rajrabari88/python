'''
• Write python program that user to enter only odd numbers, else will
raise an exception.

'''
def get_odd_number():
    while True:
        try:
            number = int(input("Enter an odd number: "))
            if number % 2 == 0:
                raise ValueError("Even number entered. Please enter an odd number.")
            return number
        except ValueError as ve:
            print(ve)

odd_number = get_odd_number()
print("You entered:", odd_number)
