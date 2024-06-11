'''
 Write a Python program to print all unique values in a dictionary.
'''


my_dict = {'a': 100, 'b': 200, 'c': 100, 'd': 300, 'e': 200, 'f': 400}
unique_values = set(my_dict.values())
print("Unique values in the dictionary:")
for value in unique_values:
    print(value)
