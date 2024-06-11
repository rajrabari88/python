'''
• Write a Python program to count the number of lines in a text file.

'''

def count_lines_in_file(filename):
    line_count = 0
    with open(filename, 'r') as file:
        for line in file:
            line_count += 1

    return line_count


filename = 'example.txt' 
num_lines = count_lines_in_file(filename)
print(f"The file '{filename}' has {num_lines} lines.")
