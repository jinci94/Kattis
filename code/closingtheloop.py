N = int(input())
x = 1
for i in range(N):
    S = int(input())
    L = input().split()
    BR = {'B': [], 'R':[]}
    for l in L:
        BR[l[-1]] += [int(l[:-1])]
    count = 0
    for b,r in zip(sorted(BR['B'], reverse=True), sorted(BR['R'], reverse=True)):
        count += b+r-2
    print(f'Case #{x}: {count}')
    x += 1