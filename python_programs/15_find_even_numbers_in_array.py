"""
Program to find all the even numbers in a given array.
"""
def find_even(arr):
    n=len(arr)
    even_arr=[]
    for i in range(0,n):
        if arr[i]%2==0:
            even_arr.append(arr[i])
    return even_arr

arr=[1,2,3,4,5,6]
even_arr=find_even(arr)
print(even_arr)