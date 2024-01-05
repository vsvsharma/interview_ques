class Solution():
    def add_binary(self,a,b):
        int_a=int(a,2)
        int_b=int(b,2)

        result_int=int_a+int_b
        result_binary=bin(result_int)[2:]
        return result_binary

a1, b1="11","1"
a2, b2="1010", "1011"
obj=Solution()
result1=obj.add_binary(a1,b1)
result2=obj.add_binary(a2,b2)
print(result1)
print(result2)
