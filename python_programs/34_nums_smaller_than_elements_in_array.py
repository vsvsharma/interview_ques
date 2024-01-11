"""
Program to find the number of elements smaller than the elements present in an array.
URL(https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/)
"""
def smallerNumbersThanCurrent(nums):
        result=[]
        for i in range(len(nums)):
            count=sum(1 for num in nums if num<nums[i])
            result.append(count)
        return result

nums=[4,6,5,8]
count=smallerNumbersThanCurrent(nums)
print(count)