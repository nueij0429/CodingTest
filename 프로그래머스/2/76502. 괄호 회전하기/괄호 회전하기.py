from collections import deque

def is_valid(s):
    stack = []
    pair = { ')':'(', '}':'{', ']':'['}
    
    for char in s:
        if char in '([{':
            stack.append(char)
        else:
            if not stack or stack[-1] != pair[char]:
                return False
            stack.pop()
    return not stack
    
def solution(s):
    dq = deque(s)
    count = 0
    
    for i in range(len(s)):
        if is_valid(dq):
            count += 1
        dq.rotate(-1)
    return count
    
    
    return answer