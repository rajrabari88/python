'''
 Explain Inheritance in Python with an example? What is init? Or What 
Is A Constructor In Python?
'''

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass  

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

dog = Dog("hari")
cat = Cat("tuntun")

print(dog.name)  
print(cat.sound()) 
