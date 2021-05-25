N = int(input())
for i in range(N):
    n, e = [int(x) for x in input().split()]
    p = 2
    while n%p != 0:
        p += 1
    q = n//p
    Eulers_totient = (p-1)*(q-1)
    d = 2
    while (d*e)%Eulers_totient != 1:
        d += 1
    print(d)