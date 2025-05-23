T = int(input())
def dfs(N):
    global count
    count += 1
    if N in graph:
        for i in graph[N]:
            dfs(i)
    else:
        return
    
for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    
    graph = dict()
    
    for i in range(0, len(arr), 2):
        if arr[i] in graph:
            graph[arr[i]].append(arr[i + 1])
        else:
            graph[arr[i]] = [arr[i + 1]]
            
    count = 0
    dfs(N)
    print(f"#{test_case} {count}")