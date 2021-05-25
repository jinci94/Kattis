N, L = [int(x) for x in input().split()]
trafficlights = [[int(x) for x in input().split()] for i in range(N)]
time = 0
x = 0
while x<L:
    if len(trafficlights) == 0 or x < trafficlights[0][0]:
        x += 1
    elif x == trafficlights[0][0] and time%(trafficlights[0][1]+trafficlights[0][2])>=trafficlights[0][1]:
        x += 1
        trafficlights.pop(0)
    time += 1
print(time)

