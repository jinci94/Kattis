
def distance_squared(p, q):
    x1, y1 = p
    x2, y2 = q
    return (x2-x1)**2 + (y2-y1)**2

coordinates = sorted([[int(x) for x in input().split()] for i in range(3)], key=lambda x:x[0])
d = [distance_squared(coordinates[i], coordinates[(i+1)%3]) for i in range(3)]
sidelength = min(d)
middle = [coordinates[(i-1)%3] for i,x in enumerate(d) if x!=sidelength][0]
sides = [coordinates[(i-1)%3] for i,x in enumerate(d) if x==sidelength]

X = sorted(sides, key=lambda x:x[0])
Y = sorted(sides, key=lambda x:x[1])
if middle[1] <= sides[0][1] and middle[1] <= sides[1][1]:
    [print(X[0][i] + X[1][i] - middle[i], end=' ') for i in range(2)]
elif middle[1] >= sides[0][1] and middle[1] >= sides[1][1]:
    [print(X[1][i] + X[0][i] - middle[i], end=' ') for i in range(2)]
elif middle[0] <= sides[0][0] and middle[0] <= sides[1][0]:
    [print(Y[0][i] + Y[1][i] - middle[i], end=' ') for i in range(2)]
elif middle[0] >= sides[0][0] and middle[0] >= sides[1][0]:
    [print(Y[1][i] + Y[0][i] - middle[i], end=' ') for i in range(2)]
