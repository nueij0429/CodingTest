def solution(brown, yellow):
    
    total = brown + yellow
    
    for length in range(3, total+1):
        if total % length == 0:
            width = total // length
            if(width-2) * (length-2) == yellow:
                return [width, length]