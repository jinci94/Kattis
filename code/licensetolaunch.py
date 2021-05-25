N = int(input())
x = [int(x) for x in input().split()]
lowest = min(x)
print(x.index(lowest))