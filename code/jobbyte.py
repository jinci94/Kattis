# Problem B: Jobbyte
N = int(input())
x = [int(x) for x in input().split()]

count = 0
for i in range(N):
    while x[i] != i+1:
        xi = x[i]
        x[i], x[xi-1] = x[x[i]-1], xi
        #temp = x[i]
        #x[i] = x[x[i]-1]
        #x[temp-1] = temp
        count += 1
print(count)
