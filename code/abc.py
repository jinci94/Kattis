A, B, C = sorted([int(x) for x in input().split()])
order = input()
values = {'A':A, 'B':B, 'C':C}
print(values[order[0]], values[order[1]], values[order[2]])