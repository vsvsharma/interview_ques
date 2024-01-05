def common_elements(list1,list2):
    common_elements=[]
    for item in list1:
        if item in list2:
            common_elements.append(item)
    return common_elements

list1=[1,2,3,4,5]
list2=[2,6,3,7,8]
result=common_elements(list1,list2)
print(result)