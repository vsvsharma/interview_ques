"""
Program to count and return the consonants in the string using recursion.
"""
def check_consonants(string):
    consonants={'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 
                'l', 'm', 'n', 'p', 'q', 'r', 's', 't',
                  'v', 'w', 'x', 'y', 'z'}
    
    if not string:
        return 0
    elif string[0].lower() in consonants:
        return 1 + check_consonants(string[1:])
    else:
        return check_consonants(string[1:])

str1="hello"
str2="Varun"
print(check_consonants(str1))
print(check_consonants(str2))
