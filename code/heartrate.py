
N = int(input())

for i in range(N):
    b, p = [float(x) for x in input().split()]
    print(round(60*(b-1)/p, 4), round(60*b/p, 4), round(60*(b+1)/p, 4))

