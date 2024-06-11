'''
• Write a Python function that checks whether a passed string is 
palindrome or not
'''
def palindrome(s):
        s = ''.join(char.lower() for char in s if char.isalnum())
        return s == s[::-1]

print(palindrome("radar"))     
print(palindrome("A man, a plan, a canal, Panama")) 
print(palindrome("hello"))   
