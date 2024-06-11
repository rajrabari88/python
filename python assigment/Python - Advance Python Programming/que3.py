'''
• Write a Python program to append text to a file and display the text.
'''


def append_to_file(filename, text_to_append):
    
    with open(filename, 'a') as file:
        file.write(text_to_append)
    print("Appended text:")
    print(text_to_append)

filename = 'example.txt'
text_to_append = "\nThis is some additional text appended to the file."
append_to_file(filename, text_to_append)
