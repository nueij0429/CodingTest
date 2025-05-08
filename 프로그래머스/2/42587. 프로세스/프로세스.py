from collections import deque

def solution(priorities, location):
    dq = deque()
    count = 0
    for i in range(len(priorities)):
        dq.append((priorities[i],i))
    
    while dq:
        max_pri = max(dq)[0]
        process = dq.popleft()
        if process[0]==max_pri:
            count+=1 
            if process[1] ==location:
                return count
        else:
            dq.append(process)
    return count