"""
Program to find and remove the duplicates from the list.
"""
def remove_duplicates(numbers):
    unique_elements=[]
    for num in numbers:
        if num not in unique_elements:
            unique_elements.append(num)
    return unique_elements

numbers=[1,1,2,4,3,6,3,5,1,6]
result=remove_duplicates(numbers)
print(result)
