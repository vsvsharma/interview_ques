"""
Problems URL(https://leetcode.com/problems/sort-the-people/description/)
"""
def sort_people(names,heights):
    sorted_data=sorted(zip(names,heights), key=lambda x:x[-1])
    sorted_names=[name for name, height in sorted_data]
    return sorted_names

names1 = ["Mary","John","Emma"]
heights1 = [180,165,170]
obj1=sort_people(names1,heights1)
print(obj1)

names2 = ["Alice","Bob","Bob"]
heights2 = [155,185,150]
obj2=sort_people(names2,heights2)
print(obj2)