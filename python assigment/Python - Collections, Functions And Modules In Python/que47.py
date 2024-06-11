'''
• Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string. 
'''


sample_string = 'rajrabari8841'
letter_count = {}
for char in sample_string:
   letter_count[char] = letter_count.get(char, 0) + 1
print("Resulting dictionary:")
print(letter_count)
