N, M = [int(x) for x in input().split()]
"""
mid = ((N+1)+(M+1))/2
if mid%2 == 0:
    start = mid - abs(N-M) + 1
    end = mid + abs(N-M)
    for x in range(start, end):
        print(x)
"""

x = {}
for i in range(1, N+1):
    for j in range(1, M+1):
        if i+j in x:
            x[i+j] += 1
        else:
            x[i+j] = 1
y = sorted([(b,a) for (a,b) in list(x.items())])
maximum = max([i[0] for i in y])
values = [i[1] for i in y if i[0]==maximum]
for value in values:
    print(value)