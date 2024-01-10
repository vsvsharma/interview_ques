"""
remove vowels from a string.
"""
def remov_vowel(str):
    vowels="aeiouAEIOU"
    result_str=""
    for char in str:
        if char not in vowels:
            result_str += char
    return result_str

str="my name is varun"
consonant_str=remov_vowel(str)
print(consonant_str)