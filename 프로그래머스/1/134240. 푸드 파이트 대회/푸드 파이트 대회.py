def solution(food):
    answer = ''
    left = ''
    
    for i in range(1, len(food)):
        foods = food[i] // 2
        left += str(i) * foods
        
        answer = left + "0" + left[::-1]
        
    return answer