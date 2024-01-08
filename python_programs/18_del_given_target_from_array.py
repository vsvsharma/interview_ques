"""
Program to delete the given targeted element from an array.
"""
def del_target(arr,target):
    n=len(arr)
    for i in range(0,n):
        if arr[i]==target:
            arr.pop(i)
    return arr

arr=[1,6,2,4,7,5]
target_element=4
updated_arr=del_target(arr,target_element)
print(updated_arr)