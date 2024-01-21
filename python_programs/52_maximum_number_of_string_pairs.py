"""
Programs URL(https://leetcode.com/problems/find-maximum-number-of-string-pairs/description/)
"""
def max_pairs(words):
    word_set = set(words)
    pairs = 0

    for word in words:
        reversed_word = word[::-1]
        if reversed_word in word_set and word != reversed_word:
            pairs += 1
            word_set.remove(word)
            word_set.remove(reversed_word)

    return pairs


words1 = ["cd", "ac", "dc", "ca", "zz"]
print(max_pairs(words1))  # Output: 2

words2 = ["ab", "ba", "cc"]
print(max_pairs(words2))  # Output: 1

words3 = ["aa", "ab"]
print(max_pairs(words3))  # Output: 0
