"""
Program to find the largest element in the list
"""
class Solution():
    def findlargest(self,numbers):
        largest=numbers[0]
        for num in numbers:
            if num>largest:
                largest=num
        return largest
        
numbers=[10,5,20,8,3]
obj=Solution()
result=obj.findlargest(numbers)
print(result)
        