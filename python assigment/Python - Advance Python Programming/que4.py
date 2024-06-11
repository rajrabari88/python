'''
Write a Python program to read first n lines of a file.


'''
def read_first_n_lines(filename, n):
    
    lines = []   
    with open(filename, 'r') as file:
        
        for _ in range(n):
            line = file.readline()
            if not line:
                break  
            lines.append(line.strip())  
    
    return lines


filename = 'example.txt'  
num_lines = 3
first_n_lines = read_first_n_lines(filename, num_lines)
print(f"First {num_lines} lines of the file:")
for line in first_n_lines:
    print(line)
