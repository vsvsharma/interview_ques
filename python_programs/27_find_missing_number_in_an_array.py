"""
Program to find the missing number from an array.
"""
def missing_num(arr):
    n=len(arr)+1
    expected_sum=n*(n+1)//2
    actual_sum=0
    for num in arr:
        actual_sum += num
    missing_number=expected_sum - actual_sum
    return missing_number

arr=[1,2,4,6,7,5]
result=missing_num(arr)
print(result)
