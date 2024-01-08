"""
Program to find the missing element in a sorted array
"""
def find_missing(num):
    n=len(num)
    for i in range(n):
        expected_value=i+1
        if num[i] != expected_value:
            return expected_value
    return n+1

num=[1,2,3,4,6]
result=find_missing(num)
print(result)