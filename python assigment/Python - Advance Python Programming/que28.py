'''
 What is used to check whether an object o is an instance of class A?
 '''


class A:
    pass
obj = A()
if isinstance(obj, A):
    print("obj is an instance of class A")
else:
    print("obj is not an instance of class A")
