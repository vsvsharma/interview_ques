"""
Problems URL(https://leetcode.com/problems/first-letter-to-appear-twice/description/)
"""
def repeatedCharacter(self, s):
        letter_indices = {}

        for index, letter in enumerate(s):
            if letter in letter_indices:
                return letter  
            else:
                letter_indices[letter] = index