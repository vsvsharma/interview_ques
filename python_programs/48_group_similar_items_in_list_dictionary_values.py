"""
Program to group all the similar values in a list with key and values in dictionary.
"""
from collections import defaultdict

def group_values(lst):
    res=defaultdict(list)
    for i in lst:
        res[i].append(i)
    return res

lst=[7,7,7,5,5,5,8,8,3,3,4,4]
obj=group_values(lst)
print(obj)