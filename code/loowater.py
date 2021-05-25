n, m = [int(x) for x in input().split()]
while n != 0 and m != 0:
    heads = sorted([int(input()) for i in range(n)])
    knights = sorted([int(input()) for i in range(m)])
    if n > m:
        print('Loowater is doomed!')
    else:
        k = 0; h = 0
        killed = 0; coins = 0
        while killed != n and k < m:
            if knights[k] >= heads[h]:
                coins += knights[k]
                killed += 1
                h += 1
            k += 1
            
        if killed == n:
            print(coins)
        else:
            print('Loowater is doomed!')

    n, m = [int(x) for x in input().split()]
