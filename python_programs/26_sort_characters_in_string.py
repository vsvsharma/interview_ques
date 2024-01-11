"""
Program to sort characters present in a String in ascending order.
"""
def sort_char_string(str):
    list_str=list(str)
    n=len(list_str)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if list_str[j]>list_str[j+1]:
                list_str[j],list_str[j+1]=list_str[j+1],list_str[j]
    sorted_str=''.join(list_str)
    return sorted_str

str="varun is good boy"
result=sort_char_string(str)
print(result)
