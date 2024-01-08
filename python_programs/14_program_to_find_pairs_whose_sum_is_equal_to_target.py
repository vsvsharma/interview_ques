"""
Program to find pairs in a  array whose sum is equal to the given target.
"""
def find_pair(arr,target):
    n=len(arr)
    pairs=[]
    for i in range(n-1):
        for j in range(i,n):
            if arr[i]+ arr[j]==target:
               pairs.append((arr[i],arr[j]))
    return pairs
            
arr=[1,2,3,4,5,6]
target=7
pairs=find_pair(arr,target)
print(pairs)