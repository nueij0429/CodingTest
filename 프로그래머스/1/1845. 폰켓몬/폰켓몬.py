from collections import Counter

def solution(nums):
    counter = Counter(nums)
    
    return min(len(nums)//2, len(counter))