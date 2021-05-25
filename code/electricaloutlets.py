N = int(input())

for i in range(N):
    x = [int(x) for x in input().split()][1:]
    print(sum(x)-len(x)+1)
