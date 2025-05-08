def solution(strings, n):
    strings.sort(key=lambda x: (x[n], x))
    # x = "sun" → x[n] = "u"
    # x = "bed" → x[n] = "e"
    # x = "car" → x[n] = "a"
    
    return strings