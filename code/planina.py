N = int(input())

start = 2
for i in range(N):
    start = 2*start - 1
print(start**2)