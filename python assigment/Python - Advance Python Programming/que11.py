'''
Write a Python program to write a list to a file.
'''

def write_list_to_file(filename, input_list):
    with open(filename, 'w') as file:
        file.writelines(str(item) + '\n' for item in input_list)

filename = 'output.txt' 
my_list = ['item1', 'item2', 'item3', 'item4']
write_list_to_file(filename, my_list)
