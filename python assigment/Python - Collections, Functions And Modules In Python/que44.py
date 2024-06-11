'''
• Write a Python program to create and display all combinations of letters, 
selecting each letter from a different key in a dictionary.
'''


from itertools import product
data = {'1': ['a', 'b'], '2': ['c', 'd']}
combinations = [''.join(comb) for comb in product(*data.values())]
print("All combinations of letters:")
for combination in combinations:
    print(combination)
