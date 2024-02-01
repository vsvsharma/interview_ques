"""
Problems URL(https://leetcode.com/problems/destination-city/description/)
"""
def destination_city(paths):
    s=set()
    for path in paths:
        s.add(path[0])

    for path in paths:
        if path[1] not in s:
            return path[1]
        
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
obj=destination_city(paths)
print(obj)