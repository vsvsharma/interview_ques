"""
Progam to find the odd elements in an array
"""
def find_odd(arr):
    odd_arr=[]
    n=len(arr)
    for i in range(0,n):
        if arr[i] % 2 !=0:
            odd_arr.append(arr[i])
    return odd_arr

arr=[1,6,3,4,2,5]
odd_num=find_odd(arr)
print(odd_num)