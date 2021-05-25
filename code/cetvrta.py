matrix = [[int(x) for x in input().split()] for i in range(3)]
x = [m[0] for m in matrix]
y = [m[1] for m in matrix]
cord_x = 0
cord_y = 0
for i in range(3):
    if x.count(x[i]) == 1:
        cord_x = x[i]
    if y.count(y[i]) == 1:
        cord_y = y[i]
print(cord_x, cord_y)
