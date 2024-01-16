"""
Problems URL(https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/description/)
"""
class Solution(object):
    def sumCounts(self, nums):
        n=len(nums)
        result=0
        for i in range(n):
            distinct_count=set()
            for j in range(i,n):
                distinct_count.add(nums[j])
                result += len(distinct_count) ** 2
        return result
        