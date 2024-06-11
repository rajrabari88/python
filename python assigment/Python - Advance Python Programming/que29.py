'''
 What relationship is appropriate for Student and Person?
'''

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

class Student:
    def __init__(self, person, student_id):
        self.person = person
        self.student_id = student_id
