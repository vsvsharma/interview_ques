"""
Program to sort the keys of the dictionary.
"""
def sort_keys_in_dict(myDict):
    my_keys=list(myDict.keys())
    my_keys.sort()
    sorted_dict={i:myDict[i] for i in my_keys}
    return sorted_dict

myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}

result=sort_keys_in_dict(myDict)
print(result)

"""
program to sort the values of the dictionary.
"""
def sort_values_in_dict(myDict):
    my_item=list(myDict.items())
    my_item.sort(key= lambda x:x[1])
    sorted_dict=dict(my_item)
    return sorted_dict

result1=sort_values_in_dict(myDict)
print(result1)