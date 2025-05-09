def solution(s):
    answer = ''
    
    for i in range(len(s)):
        sorted_s = sorted(s, reverse=True)
        answer = "".join(sorted_s)
    
    return answer