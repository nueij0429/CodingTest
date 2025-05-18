def solution(s):
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack: #스택이 비어있다면
                return False
            stack.pop()
            
    return len(stack) == 0