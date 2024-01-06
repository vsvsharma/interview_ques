"""
Program to reverse an array without using inbuilt reverse function.
"""
def reverse_array(arr):
    start=0
    end=len(arr)-1

    while start<end:
        arr[start], arr[end]= arr[end],arr[start]

        start +=1
        end -=1
    return arr

arr=[1,2,3,4,5,6]
reversed_arr=reverse_array(arr)
print(reversed_arr)
