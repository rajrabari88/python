'''
 Write a Python program to find the highest 3 values in a dictionary
'''

my_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}
sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
highest_3_values = sorted_dict[:3]
print("Highest 3 values in the dictionary:")
for key, value in highest_3_values:
    print(f"{key}: {value}")
