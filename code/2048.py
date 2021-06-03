grid = [[int(x) for x in input().split()] for _ in range(4)]
pos = int(input())

if pos == 0: # left
    def loop(i,j):
        for k in range(j, 3):
            grid[i][k] = grid[i][k+1]
        grid[i][-1] = 0
    for i in range(4):  # all rows
        while grid[i][0] == 0 and sum(grid[i][:]) != 0:
                loop(i,0)
        for j in range(3):
            while grid[i][j+1] == 0 and sum(grid[i][j+1:]) != 0:
                loop(i,j+1)
            if grid[i][j] == grid[i][j+1]:
                grid[i][j] *= 2
                grid[i][j+1] = 0
                #loop(i,j+1)
            while grid[i][j+1] == 0 and sum(grid[i][j+1:]) != 0:
                loop(i,j+1)
        

elif pos == 1: # up
    def loop(i,j):
        for k in range(i, 3):
            grid[k][j] = grid[k+1][j]
        grid[-1][j] = 0
    for j in range(4):  # all columns
        while grid[0][j] == 0 and sum([grid[l][j] for l in range(4)]) != 0:
                loop(0,j)
        for i in range(3):
            while grid[i+1][j] == 0 and sum([grid[l][j] for l in range(i+1, 4)]) != 0:
                loop(i+1,j)
            if grid[i][j] == grid[i+1][j]:
                grid[i][j] *= 2
                grid[i+1][j] = 0
                #loop(i+1,j)
            while grid[i+1][j] == 0 and sum([grid[l][j] for l in range(i+1, 4)]) != 0:
                loop(i+1,j)

elif pos == 2: # right
    def loop(i,j):
        for k in range(j,0,-1):
            grid[i][k] = grid[i][k-1]
        grid[i][0] = 0
    for i in range(4):  # all rows
        while grid[i][-1] == 0 and sum(grid[i][:]) != 0:
                loop(i,3)
        for j in range(3,0,-1):
            while grid[i][j-1] == 0 and sum(grid[i][:j-1]) != 0:
                loop(i,j-1)
            if grid[i][j] == grid[i][j-1]:
                grid[i][j] *= 2
                grid[i][j-1] = 0
            while grid[i][j-1] == 0 and sum(grid[i][:j-1]) != 0:
                loop(i,j-1)

elif pos == 3: # down
    def loop(i,j):
        for k in range(i,0,-1):
            grid[k][j] = grid[k-1][j]
        grid[0][j] = 0
    for j in range(4):  # all columns
        while grid[-1][j] == 0 and sum([grid[l][j] for l in range(4)]) != 0:
                loop(3,j)
        for i in range(3,0,-1):
            while grid[i-1][j] == 0 and sum([grid[l][j] for l in range(i-1)]) != 0:
                loop(i-1,j)
            if grid[i][j] == grid[i-1][j]:
                grid[i][j] *= 2
                grid[i-1][j] = 0
                #loop(i-1,j)
            while grid[i-1][j] == 0 and sum([grid[l][j] for l in range(i-1)]) != 0:
                loop(i-1,j)

for row in grid:
        print(' '.join(map(str, row)))