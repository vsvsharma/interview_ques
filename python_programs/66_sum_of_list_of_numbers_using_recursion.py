"""
Python Program to find the sum of list of numbers using recursion.
"""
def listsum(numbers):
    if not numbers:
        return 0
    else:
        return numbers[0] + listsum(numbers[1:])

my_list=[1,2,3,4,5]
obj=listsum(my_list)
print(f"sum of numbers in the list: {obj}")