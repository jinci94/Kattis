N = int(input())

for i in range(N):
    r, e, c = [int(x) for x in input().split()]
    if r == e-c:
        print('does not matter')
    elif r < e-c:
        print('advertise')
    elif r > e-c:
        print('do not advertise')

