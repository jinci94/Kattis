P = int(input())
for i in range(P):
    K, N = [int(x) for x in input().split()]
    count = 0
    for j in range(N):
        count += j+2

    print(K, count)