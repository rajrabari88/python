#Write a Python program to remove an empty tuple(s) from a list of tuples.


tuple_list=[(310,11),(),(45,8421,1),()]

def empty(tuple):
    return [ item for item in tuple_list if item]

remove_empty=empty(tuple_list)
print(remove_empty)
