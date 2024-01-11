"""
Program to find the if jewel has the stone which are declared under the stones.
URL(https://leetcode.com/problems/jewels-and-stones/description/)
"""
def find_jewel_stone(jewels,stones):
    jewel_set=set(jewels)
    count=0
    for stone in stones:
        if stone in jewel_set:
            count +=1
    return count

jewels="aA"
stones="aAAbbb"
result=find_jewel_stone(jewels,stones)
print(result)