
def next_step(matrix, before, next):
    if matrix[next[1]][next[0]] == 'x':
        return next
    elif matrix[next[1]][next[0]] == '/':
        if before[0] < next[0]:
            return next_step(matrix, next, [next[0],next[1]-1])
        elif before[0] > next[0]:
            return next_step(matrix, next, [next[0],next[1]+1])
        elif before[1] < next[1]:
            return next_step(matrix, next, [next[0]-1,next[1]])
        elif before[1] > next[1]:
            return next_step(matrix, next, [next[0]+1,next[1]])
    elif matrix[next[1]][next[0]] == '\\':
        if before[0] < next[0]:
            return next_step(matrix, next, [next[0],next[1]+1])
        elif before[0] > next[0]:
            return next_step(matrix, next, [next[0],next[1]-1])
        elif before[1] < next[1]:
            return next_step(matrix, next, [next[0]+1,next[1]])
        elif before[1] > next[1]:
            return next_step(matrix, next, [next[0]-1,next[1]])
    else:   # must be '.', since we started on '*'
        if before[0] < next[0]:
            return next_step(matrix, next, [next[0]+1,next[1]])
        elif before[0] > next[0]:
            return next_step(matrix, next, [next[0]-1,next[1]])
        elif before[1] < next[1]:
            return next_step(matrix, next, [next[0],next[1]+1])
        elif before[1] > next[1]:
            return next_step(matrix, next, [next[0],next[1]-1])

W, L = [int(x) for x in input().split()]
nr = 1
while W != 0 and L != 0:
    print('HOUSE', nr)
    house = [input() for j in range(L)]
    
    for i in range(L):
        for j in range(W):
            if house[i][j] == '*':
                w = j; l = i
    if l == 0:
        coordinates = next_step(house, [w,l], [w,l+1])
    elif l == L-1:
        coordinates = next_step(house, [w,l], [w,l-1])
    elif w == 0:
        coordinates = next_step(house, [w,l], [w+1,l])
    elif w == W-1:
        coordinates = next_step(house, [w,l], [w-1,l])

    for i in range(len(house)):
        for j in range(len(house[i])):
            if coordinates == [j,i]:
                print('&', end='')
            else:
                print(house[i][j], end='')
        print()

    W, L = [int(x) for x in input().split()]
    nr += 1

