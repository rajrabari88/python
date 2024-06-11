'''
Write a Python program to read a file line by line store it into a variable.
'''

def read_file_into_variable(filename):
    file_contents = ""
    with open(filename, 'r') as file:
        for line in file:
            file_contents += line

    return file_contents

filename = 'example.txt'  
contents = read_file_into_variable(filename)
print("Contents of the file stored in a variable:")
print(contents)
