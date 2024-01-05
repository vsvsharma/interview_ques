"""
 Python program to sort a list of elements using the bubble sort algorithm.
"""
def bubble_sort(numbers):
    n=len(numbers)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if numbers[j]>numbers[j+1]:
                numbers[j],numbers[j+1]= numbers[j+1],numbers[j]
    return numbers
        
numbers=[1,3,6,5,2,7,4]
sorted=bubble_sort(numbers)
print(sorted)
                

