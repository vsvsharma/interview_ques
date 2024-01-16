"""
Problems URL(https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true)
"""
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    totalapples=totaloranges=0
    for i in range(len(apples)):
        if s<= a+apples[i] <=t:
            totalapples +=1
    for j in range(len(oranges)):
        if s<= b+oranges[j] <=t:
            totaloranges +=1
            
    print(totalapples)
    print(totaloranges)