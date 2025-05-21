from collections import Counter

def solution(k, tangerine):
    size_count = Counter(tangerine)
    sorted_counts = sorted(size_count.values(), reverse = True)
    
    count = 0
    kind = 0
    
    for c in sorted_counts:
        count += c
        kind += 1
        
        if count >= k:
            break
            
    return kind