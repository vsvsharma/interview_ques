"""
Program to return all the non repeating characters in a string.
"""
def non_repeating(str):
    freq_dict={}
    for char in str:
        if char in freq_dict:
            freq_dict[char] +=1
        else:
            freq_dict[char]=1
    
    non_repeating_str=""
    for char in str:
        if freq_dict[char]==1:
            non_repeating_str += char
    return freq_dict,non_repeating_str

str="happy"
result=non_repeating(str)
print(result)

    