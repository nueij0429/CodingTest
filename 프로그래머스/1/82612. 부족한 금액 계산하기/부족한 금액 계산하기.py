def solution(price, money, count):
    total = 0
    
    for i in range(1, count+1):
        total += price * i
        
    minus = total - money
    
    return minus if minus > 0 else 0