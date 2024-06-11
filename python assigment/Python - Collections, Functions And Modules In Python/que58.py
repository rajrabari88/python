'''
 Write a Python program to convert degree to radian
'''
import math

def degrees_to_radians(degrees):   
    return degrees * math.pi / 180
degrees = 90
radians = degrees_to_radians(degrees)
print(f"{degrees} degrees is equal to {radians:.2f} radians.")

