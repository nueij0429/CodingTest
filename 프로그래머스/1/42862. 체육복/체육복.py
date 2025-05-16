def solution(n, lost, reserve):
    set_lost = set(lost)
    set_reserve = set(reserve)
    unresolved = 0
    
    real_lost = set_lost - set_reserve
    real_reserve = set_reserve - set_lost
    
    real_lost = sorted(real_lost)
    real_reserve = sorted(real_reserve)
    
    for num in real_lost:
        if num-1 in real_reserve:
            real_reserve.remove(num-1)
        elif num+1 in real_reserve:
            real_reserve.remove(num+1)
        else:
            unresolved += 1
            
    return n - unresolved