"""
Problems URL(https://leetcode.com/problems/single-number/description/)
"""
def singleNumber(nums):
    
    unique_sum = sum(set(nums))
    
    total_sum = sum(nums)
    
    twice_single_sum = 2 * unique_sum
    
    return twice_single_sum - total_sum

nums1 = [2, 2, 1]
nums2 = [4, 1, 2, 1, 2]
nums3 = [1]

print(singleNumber(nums1))
print(singleNumber(nums2))  
print(singleNumber(nums3))  
