"""
Program to find the frequency of each element present in the list or a string.
"""
def freq_of_each_element(number):
    frequency={}
    for num in number:
        if num in frequency:
            frequency[num] +=1
        else:
            frequency[num]=1
    return frequency

#number=[1,2,1,5,4,5,2,3,5]
number="NYKAA"
result=freq_of_each_element(number)
print(result)