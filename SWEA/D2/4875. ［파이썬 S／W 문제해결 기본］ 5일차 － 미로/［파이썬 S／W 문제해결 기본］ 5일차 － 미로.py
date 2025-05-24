def dfs(y, x):
    global answer
    data[y][x] = 1
    for d in range(4):
        xf = dx[d] + x
        yf = dy[d] + y
        
        if (0 <= xf < N) and (0 <= yf < N):
            if data[yf][xf] == 0:
                dfs(yf, xf)
            if data[yf][xf] == 3:
                answer = 1
                return
        
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                x = j
                y = i
                
    answer = 0
    dfs(y, x)
    
    print(f'#{test_case} {answer}')
