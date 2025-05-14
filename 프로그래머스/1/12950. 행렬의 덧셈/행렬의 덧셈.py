def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)): #열 구하기
        row = []
        for j in range(len(arr1[0])): #행 구하기
            row.append(arr1[i][j] + arr2[i][j])
        answer.append(row)
    
    return answer