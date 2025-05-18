def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j #유지된 시간 = 현재 시점-그 시점
        stack.append(i)

    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j
        
    return answer