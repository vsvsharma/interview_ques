"""
Program to insert the key and value at the beginning of the dictionary.
"""
from collections import OrderedDict

def add_element(key,value,myDict):
    myDict[key]=value
    myDict.move_to_end(key,last=False)
    return myDict

myDict=OrderedDict({'a':1, 'r':1, 'u':1, 'n':1})
key='v'
value=1
result=add_element(key,value,myDict)
print(result)