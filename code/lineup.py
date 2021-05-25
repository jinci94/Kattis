N = int(input())
names = [input() for i in range(N)]
names_increasing = sorted(names, reverse=False)
names_decreasing = sorted(names, reverse=True)
print('INCREASING') if names == names_increasing else print('DECREASING') \
    if names == names_decreasing else print('NEITHER')