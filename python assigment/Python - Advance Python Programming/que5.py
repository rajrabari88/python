'''
 Write a Python program to read last n lines of a file.
 '''
def read_last_n_lines(filename, n):
    lines = []
    with open(filename, 'r') as file:
        lines = file.readlines()
    last_n_lines = lines[-n:]
    
    return last_n_lines

filename = 'example.txt' 
num_lines = 3
last_n_lines = read_last_n_lines(filename, num_lines)
print(f"Last {num_lines} lines of the file:")
for line in last_n_lines:
    print(line.strip())

