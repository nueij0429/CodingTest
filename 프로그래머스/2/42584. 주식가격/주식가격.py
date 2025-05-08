def solution(prices):
    answer=[]
    for i in range(len(prices)): # 0-4
        current_price = prices[i]
        count = 0
        for j in range(i+1,len(prices)): # 1-4 , 2-4 , 3-4 ,4-4
            count += 1
            if prices[j] < current_price:
                break
        answer.append(count)
    answer[-1]=0
    return answer