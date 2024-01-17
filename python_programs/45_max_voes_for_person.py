"""
Program to find the maximum number of votes for person.
"""
from collections import Counter

def max_votes(arr):
    vote_count=Counter(arr)
    max_vote=max(vote_count.values())
    candidate_with_max_vote=[]
    for candidate,counts in vote_count.items():
        if counts==max_vote:
            candidate_with_max_vote.append(candidate)
    
    candidate_with_max_vote.sort()
    winner=candidate_with_max_vote[0]
    return winner

votes=['varun', 'tarun', 'kittu', 'kittu', 'varun','kittu','nitin']
result=max_votes(arr=votes)
print(result)