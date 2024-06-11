'''
• Write a Python program to read an entire text file.
'''


def read_text_file(filename):
   
    with open(filename, 'r') as file:
        file_contents = file.read()
    
    return file_contents

filename = 'example.txt' 
file_contents = read_text_file(filename)
print("Contents of the text file:")
print(file_contents)
