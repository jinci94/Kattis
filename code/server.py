n, T = [int(x) for x in input().split()]
tasks = [int(x) for x in input().split()]
time = 0; count = 0
for task in tasks:
    if task + time <= T:
        count += 1
        time += task
    else:
        break
print(count)
