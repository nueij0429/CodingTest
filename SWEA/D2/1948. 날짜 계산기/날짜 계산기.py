month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

T = int(input())
for test_case in range(1, T + 1):
    change = 1
    m1, d1, m2, d2 = list(map(int, input().split()))
    
    if m1 == m2:
        change += d2 - d1
    else:
        for i in range(m1, m2):
            change += month[i]
        change += d2 - d1
    print(f'#{test_case} {change}')