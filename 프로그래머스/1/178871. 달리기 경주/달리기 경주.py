def solution(players, callings):
    #딕셔너리 컴프리헨션
    rank = {name: i for i, name in enumerate(players)}

    for name in callings:
        i = rank[name]
        players[i-1], players[i] = players[i], players[i-1]

        rank[players[i]] = i
        rank[players[i-1]] = i - 1

    return players