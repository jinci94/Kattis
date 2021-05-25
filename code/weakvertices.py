n = int(input())
while n != -1:
    l = [[int(x) for x in input().split()] for i in range(n)]
    weak = ''
    for i in range(n):
        neighbours = [j for j,x in enumerate(l[i]) if x==1]
        nn = []
        for n in neighbours:
            nn += [j for j,x in enumerate(l[n]) if (x==1 and j in neighbours)]
        if len(nn) == 0:
            weak += str(i) + ' '
    print(weak[:-1])
    n = int(input())
