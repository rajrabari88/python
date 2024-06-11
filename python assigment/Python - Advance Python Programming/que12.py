'''
• Write a Python program to copy the contents of a file to another file.

'''
def copy_file_contents(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            contents = src.read()
        
        with open(destination_file, 'w') as dest:
            dest.write(contents)
        
        print(f"Contents of {source_file} have been copied to {destination_file}.")
    except FileNotFoundError:
        print(f"Error: {source_file} does not exist.")
    except IOError as e:
        print(f"Error: {e}")


source_file = 'source.txt'
destination_file = 'destination.txt'

copy_file_contents(source_file, destination_file)
