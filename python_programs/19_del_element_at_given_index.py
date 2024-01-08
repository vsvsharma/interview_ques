"""
Program to delete an element at a given index.
"""
def del_element_at_given_index(arr,index):
    n=len(arr)
    for i in range(0,n):
        if i==index:
            arr.pop(i)
    return arr

arr=[23,16,20,25,35,33]
targeted_index=2
updated_arr=del_element_at_given_index(arr,targeted_index)
print(updated_arr)
