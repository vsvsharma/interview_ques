"""
Program to find the number of good pairs.
URL(https://leetcode.com/problems/number-of-good-pairs/description/)
"""
class Solution(object):
    def numIdenticalPairs(self, nums):
        count_map = {}
        result = 0

        for num in nums:
            if num in count_map:
                result += count_map[num]
                count_map[num] += 1
            else:
                count_map[num] = 1

        return result
        
solution=Solution()
nums=[1,2,3,1,1,1,4,5]
pairs=solution.numIdenticalPairs(nums)
print(pairs)