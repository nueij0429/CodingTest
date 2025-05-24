T = int(input())

for test_case in range(1, T + 1):
    str = input()
    list = []
    
    for i in str:
        if list and i == list[-1]:
            list.pop()
        else:
            list.append(i)
    print(f'#{test_case} {len(list)}')
