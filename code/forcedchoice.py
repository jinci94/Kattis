N, P, S = [int(x) for x in input().split()]

for i in range(S):
    x = [int(x) for x in input().split()]
    if P in x[1:]:
        print('KEEP')
    else:
        print('REMOVE')