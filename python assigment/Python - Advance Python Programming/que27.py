'''
What is Instantiation in terms of OOP terminology?
'''
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

