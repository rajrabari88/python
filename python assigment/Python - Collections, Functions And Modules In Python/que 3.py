n = int(input("Enter the range for the Fibonacci series: "))
a, b = 0, 1
if n <= 0:
    print("Please enter positive number:")
else:
    print("Fibonacci series:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
