def solution(n):
    base3 = ''
    
    while n > 0:
        base3 = str(n % 3) + base3
        n //= 3
        
    reversed_base3 = base3[::-1]
    return int(reversed_base3, 3)