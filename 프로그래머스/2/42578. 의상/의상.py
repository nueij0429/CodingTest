def solution(clothes):
    wear = {}
    
    for name, kind in clothes:
        if kind not in wear:
            wear[kind] = 0
        wear[kind] += 1
        
    answer = 1
    
    for count in wear.values():
        answer *= (count + 1)
    
    return answer - 1 #아무것도 안 입는 경우
        