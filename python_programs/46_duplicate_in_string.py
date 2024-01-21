"""
Program to find all the duplicate characters in a string.
"""
from collections import Counter

def find_duplicate(str):
    chars={}
    for char in str:
        if char not in chars:
            chars[char]=1
        else:
            chars[char] +=1
    
    lst=[]
    for char, count in chars.items():
        if count>1:
            lst.append(char)
    return lst

obj= find_duplicate("titfortat")
print(obj)

def find_duplicate_using_counter(str1):
    counter_str=Counter(str1)
    lst2=[]
    for char, count in counter_str.items():
        if count >1:
            lst2.append(char)
    return lst2

obj2=find_duplicate_using_counter("geeksforgeeks")
print(obj2)