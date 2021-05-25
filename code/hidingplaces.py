N = int(input())

for i in range(N):
    A = 'abcdefgh'
    chess_matrix = [[0 for i in range(8)] for j in range(8)]
    col = {a:i for i,a in enumerate(A)}

    x, y = input()
    x = col[x]; y = int(y)-1
    chess_matrix[x][y] = 1
    start_list = [[x,y]]
    next_list = []; count = 0
    while sum([sum(x) for x in chess_matrix]) < 8**2:
        for start in start_list:
            if start[0] >= 1 and start[1] <= 5 and chess_matrix[start[0]-1][start[1]+2] == 0:
                chess_matrix[start[0]-1][start[1]+2] = 1
                next_list.append([start[0]-1, start[1]+2])
            if start[0] <= 6 and start[1] <= 5 and chess_matrix[start[0]+1][start[1]+2] == 0:
                chess_matrix[start[0]+1][start[1]+2] = 1
                next_list.append([start[0]+1, start[1]+2])
            if start[0] <= 5 and start[1] <= 6 and chess_matrix[start[0]+2][start[1]+1] == 0:
                chess_matrix[start[0]+2][start[1]+1] = 1
                next_list.append([start[0]+2, start[1]+1])
            if start[0] <= 5 and start[1] >= 1 and chess_matrix[start[0]+2][start[1]-1] == 0:
                chess_matrix[start[0]+2][start[1]-1] = 1
                next_list.append([start[0]+2, start[1]-1])
            if start[0] <= 6 and start[1] >= 2 and chess_matrix[start[0]+1][start[1]-2] == 0:
                chess_matrix[start[0]+1][start[1]-2] = 1
                next_list.append([start[0]+1, start[1]-2])
            if start[0] >= 1 and start[1] >= 2 and chess_matrix[start[0]-1][start[1]-2] == 0:
                chess_matrix[start[0]-1][start[1]-2] = 1
                next_list.append([start[0]-1, start[1]-2])
            if start[0] >= 2 and start[1] >= 1 and chess_matrix[start[0]-2][start[1]-1] == 0:
                chess_matrix[start[0]-2][start[1]-1] = 1
                next_list.append([start[0]-2, start[1]-1])
            if start[0] >= 2 and start[1] <= 6 and chess_matrix[start[0]-2][start[1]+1] == 0:
                chess_matrix[start[0]-2][start[1]+1] = 1
                next_list.append([start[0]-2, start[1]+1])
        start_list = next_list
        next_list = []
        count += 1
    start_list = sorted(start_list, key=lambda x: (-x[1],x[0]), reverse=False)
    print(count, ' '.join([A[x]+str(y+1) for x,y in start_list]))