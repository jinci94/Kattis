N = int(input())
while N != 0:
    n = sum([int(x) for x in str(N)])
    p = 11
    while sum([int(x) for x in str(p*N)]) != n:
        p += 1
    print(p)
    N = int(input())
