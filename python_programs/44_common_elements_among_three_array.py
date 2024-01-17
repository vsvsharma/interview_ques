"""
Program to find the common elements among all three arrays using dictionary intersection.
"""
from collections import Counter

def common_elements(ar1,ar2,ar3):
    ar1=Counter(ar1)
    ar2=Counter(ar2)
    ar3=Counter(ar3)

    resultDict=dict(ar1.items() & ar2.items() & ar3.items())
    list=[]
    for (key,val) in resultDict.items():
        for i in range(0, val):
            list.append(key)
    return list

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
result=common_elements(ar1,ar2,ar3)
print(result)