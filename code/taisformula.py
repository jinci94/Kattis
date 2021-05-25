N = int(input())
matrix = [[float(x) for x in input().split()] for i in range(N)]
A = 0
for i in range(N-1):
    A += (matrix[i][1]+matrix[i+1][1])/2 * (matrix[i+1][0] - matrix[i][0])
print(A/1000)
