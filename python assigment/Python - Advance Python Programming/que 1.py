'''
• What is File function in python? What is keywords to create and write 
file.
'''

file = open("example.txt", "w")
file.write("Hello, World!\n")
file.write("This is a sample file.\n")

file.close()
