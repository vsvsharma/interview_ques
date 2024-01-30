"""
Problems URL(https://www.hackerrank.com/challenges/whats-your-name/problem)
"""
def your_name(first,last):
    full_name=f'Hello {first} {last}! You just delved into python.'
    print(full_name)

first=input()
last=input()
obj=your_name(first,last)
