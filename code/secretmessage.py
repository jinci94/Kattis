from math import ceil, sqrt
N = int(input())
for i in range(N):
    msg_in = input()
    n = ceil(sqrt(len(msg_in)))
    matrix = [['']*n for _ in range(n)]
    k = 0
    for i in range(n):
        for j in range(n):
            if k < len(msg_in):
                matrix[i][j] = msg_in[k]
                k += 1
    matrix_rotated = [['']*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix_rotated[i][j] = matrix[n-j-1][i]
        print(''.join(matrix_rotated[i]), end='')
    print()
