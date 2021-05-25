T = int(input())
for i in range(T):
    N, M = [int(x) for x in input().split()]
    
    n = [[int(x) for x in input().split()][1:] for y in range(N)]
    m = {i: int(x) for i, x in enumerate(input().split(), start=1)}
    cash = 0
    for price in n:
        count = max([e[1] for e in list(m.items())])
        for i in price[:-1]:
            if m[i] < count:
                count = m[i]
        for i in price[:-1]:
            m[i] -= count
        cash += count*price[-1]
    print(cash)
