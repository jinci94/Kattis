N = int(input())
x = [[int(x) for x in input().split()] for i in range(N)]
greatest_speed = 0  # that we can be certain of
for x1, x2 in zip(x[:-1], x[1:]):
    speed = int((x2[1]-x1[1])/(x2[0]-x1[0]))
    if greatest_speed < speed:
        greatest_speed = speed
print(greatest_speed)