"""
Program to find the sum of all elements present in an array.
"""
def sum_of_elements(arr):
    sum=0
    for i in arr:
        sum=sum+i
    return sum

arr=[20,15,31,25,30]
sum=sum_of_elements(arr)
print(sum)