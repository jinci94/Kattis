P, N = [int(x) for x in input().split()]
w = [input() for i in range(N)]
if len(set(w)) < P:
    print('paradox avoided')
else:
    parts = []; i = 0
    while len(parts) != P:
        if w[i] not in parts:
            parts.append(w[i])
        i += 1
    print(i)