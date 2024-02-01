"""
Problems URL(https://leetcode.com/problems/find-common-elements-between-two-arrays/description/)
"""
def calculate_occurrences(nums1, nums2):
    occurrences_nums1 = sum(1 for num in nums1 if num in nums2)
    occurrences_nums2 = sum(1 for num in nums2 if num in nums1)
    return [occurrences_nums1, occurrences_nums2]

nums1_1 = [4, 3, 2, 3, 1]
nums2_1 = [2, 2, 5, 2, 3, 6]
result_1 = calculate_occurrences(nums1_1, nums2_1)
print(result_1)  # Output: [3, 4]

nums1_2 = [3, 4, 2, 3]
nums2_2 = [1, 5]
result_2 = calculate_occurrences(nums1_2, nums2_2)
print(result_2)  # Output: [0, 0]
