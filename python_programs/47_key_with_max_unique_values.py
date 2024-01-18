"""
Program to find the key with the most unique value.
"""

def unique_key(test_dict):
    max_value=0
    max_key=None
    for key,values in test_dict.items():
        unique_value_count=len(set(values))
        if unique_value_count > max_value:
            max_value=unique_value_count
            max_key=key
    return max_key

test_dict={
    "vs_code":[1,2,3,1,2],
    "is":[1,2,3,2,5],
    "best":[2,3,2,4]
}
obj= unique_key(test_dict)
print(obj)