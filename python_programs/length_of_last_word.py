class Solution:
    def length_of_last_word(self,s):
        words=s.split()
        if not words:
            return 0
        
        return len(words[-1])
    
s1="hello world"
s2="name is varun"
s3="length of last word"    
obj=Solution()
print(obj.length_of_last_word(s1))
print(obj.length_of_last_word(s2))
print(obj.length_of_last_word(s3))