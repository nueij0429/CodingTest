T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [[0] * N for _ in range(N)]
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y, d = 0, 0, 0
    
    for num in range(1, N * N + 1):
        matrix[x][y] = num
        
        nx =  dx[d] + x
        ny = dy[d] + y
        
        if nx < 0 or ny < 0 or nx >= N or ny >= N or matrix[nx][ny] != 0:
            d = (d + 1) % 4
            nx =  dx[d] + x
            ny = dy[d] + y
        x, y = nx, ny
        
    print(f"#{test_case}")
    for row in matrix:
        print(' '.join(map(str, row)))