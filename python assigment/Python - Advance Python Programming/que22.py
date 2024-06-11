'''
• How to Define a Class in Python? What Is Self? Give An Example Of 
A Python Class
'''

class Dog:
    species = "Canine"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        return f"{self.name} is {self.age} years old"
    def speak(self, sound):
        return f"{self.name} says {sound}"
dog1 = Dog("rocy", 3)
dog2 = Dog("tuntun", 5)

print(dog1.description())  
print(dog2.speak("Woof")) 
