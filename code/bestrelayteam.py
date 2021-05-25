
runners = {}
N = int(input())
for i in range(N):
    name, t1, t2 = input().split()
    runners[name] = (float(t1) , float(t2))

runners1 = sorted(list(runners.items()), key=lambda x:x[1][0])
runners2 = sorted(list(runners.items()), key=lambda x:x[1][1])

first_runner = [(name, time) for name, (time, _) in runners1[:4]]
other_runner = [(name, time) for name, (_, time) in runners2[:4]]

time = 20*4; names = []
for i, first in enumerate(first_runner):
    temp_names = [first[0]]; temp_time = first[1]
    for j, other in enumerate(other_runner):
        if len(temp_names) < 4 and other[0] not in temp_names:
            temp_names.append(other[0])
            temp_time += other[1]
    if time > temp_time:
        time = temp_time
        names = temp_names
        
print(time)
for name in names:
    print(name)

