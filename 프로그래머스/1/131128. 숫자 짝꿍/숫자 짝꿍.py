from collections import Counter

def solution(X, Y):
    counter_x = Counter(X)
    counter_y = Counter(Y)
    answer = []
    
    for digit in map(str, range(9, -1, -1)): # 큰 수부터 붙여야 하기 때문
        common = min(counter_x[digit], counter_y[digit])
        answer.extend([digit] * common)
        
    if not answer:
        return "-1"
    
    if answer[0] == '0':
        return "0"
    
    return ''.join(answer)