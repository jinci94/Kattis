s, t, n = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

time = s
for i in range(n):
    time += d[i]
    if time%c[i] != 0:
        time += (c[i] - time%c[i])
    time += b[i]
time += d[-1]

print('yes') if time<=t else print('no')