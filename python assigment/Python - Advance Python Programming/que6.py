'''
 Write a Python program to read a file line by line and store it into a list
 '''

def read_file_into_list(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append(line.strip())
            return lines

filename = 'example.txt'  
lines = read_file_into_list(filename)
print("Lines of the file stored in a list:")
for line in lines:
    print(line)
