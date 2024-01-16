"""
Problems URL(https://leetcode.com/problems/unique-morse-code-words/description/)
"""
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse_code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result=set()
        for word in words:
            morse=""
            for char in word:
                morse += morse_code[ord(char)-97]
            result.add(morse)
        return (len(result))