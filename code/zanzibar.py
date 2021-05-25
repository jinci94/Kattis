T = int(input())

for i in range(T):
    turtles = [int(x) for x in input().split()]
    count = 0
    for t1, t2  in zip(turtles[:-2], turtles[1:-1]):
        if t2>2*t1:
            count += t2 - 2*t1
    print(count)

