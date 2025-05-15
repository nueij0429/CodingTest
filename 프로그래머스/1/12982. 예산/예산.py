def solution(d, budget):
    count = 0
    d.sort()
    
    for cost in d:
        if budget >= cost:
            budget-=cost
            count+=1
        else:
            break
    
    return count