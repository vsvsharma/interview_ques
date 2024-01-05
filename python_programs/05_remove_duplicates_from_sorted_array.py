class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        i=0
        for j in range(1,len(nums)):
            if nums[j]!= nums[i]:
                i=i+1
                nums[i]=nums[j]
        return i+1
    
nums=[1,2,2,3,3,4,5,5,5]
obj=Solution()
result=obj.removeDuplicates(nums)
print(nums[:result])