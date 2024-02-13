"""
Program to print the fibonacci series using recursion.
"""
def fibonacci_series(n,a=0,b=1):
    if n==0:
        return
    print(a,end=" ")
    fibonacci_series(n-1,b,a+b)
    
n=10
fibonacci_series(10)   