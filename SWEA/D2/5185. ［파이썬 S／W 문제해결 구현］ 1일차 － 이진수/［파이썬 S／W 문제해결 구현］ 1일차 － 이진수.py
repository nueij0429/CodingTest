T = int(input())

trans = {'A': 10, 'B': 11, 'C':12, 'D':13, 'E':14, 'F':15}

for test_case in range(1, T + 1):
    N, nums = input().split()
    answer = ''
    
    for i in nums[::-1]:
        if i in trans:
            i = trans[i]
        i = int(i)
        
        for _ in range(4):
            answer = str(i % 2) + answer
            i //= 2
            
    print(f'#{test_case} {answer}')
