'''
 Write a Python program to calculate the area of a trapezoid
'''

def trapezoid_area(base1, base2, height):

    return 0.5 * (base1 + base2) * height


base1 = 5
base2 = 9
height = 4
area = trapezoid_area(base1, base2, height)
print(f"The area of the trapezoid is {area}.")
