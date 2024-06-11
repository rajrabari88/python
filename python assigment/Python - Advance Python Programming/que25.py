'''
• Write a Python class named Circle constructed by a radius and two 
methods which will compute the area and the perimeter of a circle
'''



class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * 3.14159 * self.radius

circle = Circle(5)

area = circle.calculate_area()
perimeter = circle.calculate_perimeter()

print("Area of the circle:", area)  
print("Perimeter of the circle:", perimeter) 
