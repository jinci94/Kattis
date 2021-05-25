x = sorted([int(x) for x in input().split()])
step = min(x[2]-x[1], x[1]-x[0])
number = 1000
for i in range(2):
    if x[i+1] != x[i]+step:
        number = x[i]+step
print(number) if number != 1000 else print(x[-1]+step)
