B, C, D, L = [int(x) for x in input().split()]
possible = False
for b in range(int(L/B)+1):
    for c in range(int((L-b*B)/C)+1):
            if (L-b*B-c*C)%D == 0:
                possible = True
                d = (L-b*B-c*C)//D
                print(b, c, d)
if not possible:
    print('impossible')