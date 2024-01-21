"""
Program to find the possible words by using a given characters.
"""
def find_possible_words(Dict,arr):
    arr_set=set(arr)
    result=[]
    for word in Dict:
        if set(word).issubset(arr_set):
            result.append(word)
    return result

Dict = ["go", "bat", "me", "eat", "goal", "boy", "run"]
arr = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
obj=find_possible_words(Dict,arr)
print(obj)