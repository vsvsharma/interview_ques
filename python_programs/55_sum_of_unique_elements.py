"""
Problems URL(https://leetcode.com/problems/sum-of-unique-elements/description/)
"""
def sum_unique_elements(nums):
    unique_set=set(nums)
    unique_elements=[num for num in unique_set if nums.count(num)==1]
    unique_sum=sum(unique_elements)
    return unique_sum

nums=[1,2,3,2]
obj=sum_unique_elements(nums)
print(obj)