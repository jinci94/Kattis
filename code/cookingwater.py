N = int(input())
timeintervalls = [[int(x) for x in input().split()] for i in range(N)]
start = max([e[0] for e in timeintervalls])
end = min([e[1] for e in timeintervalls])
print('edward is right') if end<start else print('gunilla has a point')
