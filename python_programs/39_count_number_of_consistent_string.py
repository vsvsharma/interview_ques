"""
Problems URL(https://leetcode.com/problems/count-the-number-of-consistent-strings/description/)
"""
class Solution(object):
    def countConsistentStrings(self, allowed, words):
        count=0
        for word in words:
            for char in word:
                if char not in allowed:
                    count +=1
                    break
        return (len(words)) - count