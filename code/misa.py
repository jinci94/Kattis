R, S = [int(x) for x in input().split()]
matrix = [[x for x in input()] for i in range(R)]

def neighbours(row, col):
    count = 0
    # + (u, d, l, r)
    if row != 0 and matrix[row-1][col] == 'o':
        count += 1
    if row != R-1 and matrix[row+1][col] == 'o':
        count += 1
    if col != 0 and matrix[row][col-1] == 'o':
        count += 1
    if col != S-1 and matrix[row][col+1] == 'o':
        count += 1
    # x (ul, ur, dl, dr)
    if row != 0 and col != 0 and matrix[row-1][col-1] == 'o':
        count += 1
    if row != 0 and col != S-1 and matrix[row-1][col+1] == 'o':
        count += 1
    if row != R-1 and col != 0 and matrix[row+1][col-1] == 'o':
        count += 1
    if row != R-1 and col != S-1 and matrix[row+1][col+1] == 'o':
        count += 1
    return count


seated = False
maximum = 0; index_i = 0; index_j = 0
for row, line in enumerate(matrix):
    for col, c in enumerate(line):
        if c == '.':
            n = neighbours(row, col)
            if n == 8:
                matrix[row][col] = 'o'
                seated = True
                break
            elif maximum < n:
                maximum = n
                index_i = row
                index_j = col
    if seated:
        break
    
if not seated:
    matrix[index_i][index_j] = 'o'

count = 0
for row, line in enumerate(matrix):
    for col, c in enumerate(line):
        if c == 'o':
            count += neighbours(row, col)
print(count//2)

