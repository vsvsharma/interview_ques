"""
Program to merge given two dictionaries.
"""
def merge_two_dict(dict1,dict2):
    merge_dict=dict()
    for key,value in dict1.items():
        merge_dict[key]= [value] if key not in merge_dict else merge_dict[key] + value

    for key, value in dict2.items():
        merge_dict[key]=[value] if key not in merge_dict else merge_dict[key] + value

    return merge_dict

dict1={'a':1,'b':3, 'c':4}
dict2={'d':2,'e':6,'f':7}
result=merge_two_dict(dict1,dict2)
print(result)