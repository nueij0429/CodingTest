T = [2, 4, 6, 8, 10]

def contains(i, j):
    if i in j:
        print(f'{i} => True')
    else:
        print(f'{i} => False')
        
print(T)
contains(5, T)
contains(10, T)