"""
Problems URL(https://www.hackerrank.com/challenges/py-the-captains-room/problem)
"""
k=int(input())
rooms=list(map(int, input().split()))
a=set()
b=set()
for room in rooms:
    if room not in a:
        a.add(room)
        b.add(room)
    else:
        b.discard(room)

b=list(b)
print(b[0])