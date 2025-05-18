from collections import deque
import math

def solution(progresses, speeds):
    days = []
    
    for p, s in zip(progresses, speeds):
        day = math.ceil((100 - p) / s)
        days.append(day)
        
    day_queue = deque(days)
    result = []
    
    while day_queue:
        current_day = day_queue.popleft()
        count = 1 #적어도 하나는 배포
        
        while day_queue and day_queue[0] <= current_day:
            day_queue.popleft()
            count += 1
    
        result.append(count)
    
    return result