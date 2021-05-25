N = int(input())
targets = [input().split() for i in range(N)]

M = int(input())
for i in range(M):
    x, y = [int(x) for x in input().split()]
    count = 0
    for target in targets:
        if target[0] == 'rectangle':
            x1, y1, x2, y2 = [int(a) for a in target[1:]]
            if x1 <= x <= x2 and y1 <= y <= y2:
                count += 1
        elif target[0] == 'circle':
            x1, y1, r = [int(a) for a in target[1:]]
            if (x-x1)**2 + (y-y1)**2 <= r**2:
                count += 1
    print(count)
