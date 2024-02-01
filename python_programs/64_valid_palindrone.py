"""
Problems URL(https://leetcode.com/problems/valid-palindrome/description/)
"""
def is_palindrome(s):
    # Convert to lowercase and remove non-alphanumeric characters
    modified_s = ''.join(c.lower() for c in s if c.isalnum())
    
    
    return modified_s == modified_s[::-1]

s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "

print(is_palindrome(s1))  # Output: True
print(is_palindrome(s2))  # Output: False
print(is_palindrome(s3))  # Output: True
