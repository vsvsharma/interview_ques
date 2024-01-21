"""
Program to replace the string in a list with the Kth value in the dictionary.
"""
def replace_string(lst,sub_dict,K):
    for i in range(len(lst)):
        if lst[i] in sub_dict:
            lst[i]=sub_dict[lst[i]][K]
    return lst

lst = ["Gfg", "is", "Best"]
subs_dict = {"Gfg": [5, 6, 7], "is": [7, 4, 2]}
K = 2
obj =replace_string(lst,subs_dict,K)
print(obj)