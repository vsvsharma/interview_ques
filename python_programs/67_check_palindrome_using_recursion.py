"""
Check the given number is palindrome using recursion.
"""
def is_palindrome(num):
    num_str=str(num)

    if len(num_str)<=1:
        return True
    elif num_str[0]==num_str[-1]:
        return is_palindrome(num_str[1:-1])
    else:
        return False
    
num1=12321
num2=12345
obj1=is_palindrome(num1)
obj2=is_palindrome(num2)
print(obj1)
print(obj2)