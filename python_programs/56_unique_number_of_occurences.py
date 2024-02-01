"""
Problems URL(https://leetcode.com/problems/unique-number-of-occurrences/description/)
"""
from collections import Counter
def unique_occurences(arr):
    count_dict=Counter(arr)
    unique_dict=set(count_dict.values())
    return len(count_dict)==len(unique_dict)

arr1=[1,1,1,2,3,2]
arr2=[1,2,3,1,2]
obj1=unique_occurences(arr1)
obj2=unique_occurences(arr2)
print(obj1)
print(obj2)