"""
Program to check if the given string is panagram or not.
"""
def check_pangram(str):
    letter_set=set()
    for char in str:
        if 'a'<= char<= 'z':
            letter_set.add(char)
    return len(letter_set)==26

sentence1 = "thequickbrownfoxjumpsoverthelazydog"
print(check_pangram(sentence1))  

sentence2 = "leetcode"
print(check_pangram(sentence2))  
