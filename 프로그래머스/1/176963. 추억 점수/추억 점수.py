def solution(name, yearning, photo):
    answer = []
    names = dict()
    
    #name이랑 yearning이랑 매핑
    for i in range(len(name)) :
        names[name[i]] = yearning[i]
        
    for p in photo :
        score = 0
        for p2 in p :
            if p2 in names:
                score+=names[p2]
        answer.append(score)
    
    return answer