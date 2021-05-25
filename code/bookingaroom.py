r, n = [int(x) for x in input().split()]
rooms = [int(input()) for i in range(n)]
if r == n:
    print('too late')
else:
    rooms = sorted(rooms)
    for nr in range(1,r+1):
        if nr not in rooms:
            print(nr)
            break