N = int(input())
for _ in range(N):
    x = input()
    y = input()
    z = ''
    for i, j in zip(x, y):
        z += '.' if i==j else '*'
    print(x)
    print(y)
    print(z+'\n')
