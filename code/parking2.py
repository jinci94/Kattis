N = int(input())

for i in range(N):
    n = int(input())
    x = [int(x) for x in input().split()]
    print((max(x)-min(x))*2)