M, N = [int(x) for x in input().split()]
U, L, R, D = [int(x) for x in input().split()]

for i in range(U):
    for j in range(L+N+R):
        if (i+j)%2==0:
            print('#', end='')
        else:
            print('.', end='')
    print()

for i in range(U,U+M):
    for j in range(L):
        if (i+j)%2==0:
            print('#', end='')
        else:
            print('.', end='')
    print(input(), end='')     # N characters
    for j in range(L+N,L+N+R):
        if (i+j)%2==0:
            print('#', end='')
        else:
            print('.', end='')
    print()

for i in range(U+M,U+M+D):
    for j in range(L+N+R):
        if (i+j)%2==0:
            print('#', end='')
        else:
            print('.', end='')
    print()
