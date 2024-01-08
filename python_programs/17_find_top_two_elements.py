"""
Program to find top two elements in an array.
"""
def top_two(arr):
    if len(arr)<2:
        return arr
    
    first_max=max(arr[0],arr[1])
    second_max=min(arr[0],arr[1])
    
    for i in range(2,len(arr)):
        if arr[i]>first_max:
            second_max=first_max
            first_max=arr[i]
        elif arr[i]>second_max and arr[i]!= first_max:
            second_max=arr[i]
    return(first_max,second_max)

arr=[2,8,5,3,9,10,6,22]
top_element=top_two(arr)
print(top_element)