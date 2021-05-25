R, C = [int(x) for x in input().split()]
x = [input() for i in range(R)]
squashes = [0,0,0,0,0]
for i in range(R-1):
    for j in range(C-1):
        b = x[i][j:j+2].count('#') + x[i+1][j:j+2].count('#')
        c = x[i][j:j+2].count('X') + x[i+1][j:j+2].count('X')
        if b == 0:
            squashes[c] += 1
for s in squashes:
    print(s)
