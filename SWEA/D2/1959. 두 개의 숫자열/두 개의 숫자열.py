T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    k = []
    
    if N > M:
        for i in range(0, N - M + 1):
            s = 0
            for j in range(M):
                s += a[j + i] * b[j]
            k.append(s)
            
    elif N < M:
        for i in range(M - N + 1):
            s = 0
            for j in range(N):
                s += a[j] * b[j + i]
            k.append(s)
	
    print(f'#{test_case} {max(k)}')
        