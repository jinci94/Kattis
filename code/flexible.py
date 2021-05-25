W, P = [int(x) for x in input().split()]
L = [0] + [int(x) for x in input().split()] + [W]

combinations = []
for i in range(P+1):
    for j in range(i+1,P+2):
        if L[j]-L[i] not in combinations:
            combinations.append(L[j]-L[i])
print(' '.join([str(x) for x in sorted(combinations)]))