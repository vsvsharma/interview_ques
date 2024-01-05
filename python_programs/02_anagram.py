class Solution():
    def check_anagram(self,s,t):
        return sorted(s)== sorted(t)
    
s1 = "anagram"
t1 = "nagaram"
s2="rat"
t2="car"
obj=Solution()
result1=obj.check_anagram(s1,t1)
result2=obj.check_anagram(s2,t2)
print(result1)
print(result2)   