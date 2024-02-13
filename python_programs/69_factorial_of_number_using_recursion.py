"""
Program to find the factorial of a number using recursion.
"""
def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1)
    
n=6
print(fact(n))