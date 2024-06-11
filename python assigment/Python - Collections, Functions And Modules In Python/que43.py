'''
Why Do You Use the Zip () Method in Python?
'''
'''
The zip() function in Python is used to combine multiple iterables(such as lists, tuples, or strings) element-wise into a single iterable.
'''


names = ['raj', 'hari', 'pritesh']
ages = [30, 25, 35]
for name, age in zip(names, ages):
    print(f'{name} is {age} years old')

#Creating Dictionaries
    
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print(my_dict)

#Unzipping

data = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]
names, ages = zip(*data)
print(names)
print(ages)



