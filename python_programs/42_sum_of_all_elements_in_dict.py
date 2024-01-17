"""
Program to find the sum of all elements present in the dictionary.
"""
def sum_of_elements_in_dict(myDict):
    list=[]
    for i in myDict:
        list.append(myDict[i])
    final=sum(list)
    return final

myDict={'varun': 400, 'tarun':256, 'arun':456}
result=sum_of_elements_in_dict(myDict)
print(result)