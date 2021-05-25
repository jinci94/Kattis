x = [int(x) for x in input().split()]
while x != [1, 2, 3, 4, 5]:
    for i in range(4):
        if x[i] > x[i+1]:
            x[i], x[i+1] = x[i+1], x[i]
            print(*x)