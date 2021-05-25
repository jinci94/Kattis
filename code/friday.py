T = int(input())
for i in range(T):
    D, M = [int(x) for x in input().split()]
    days = [int(x) for x in input().split()]
    start = 2; count = 0
    for day in days:
        if day >= 13 and start == 2:
            count += 1
        start = (start+day)%7
    print(count)
