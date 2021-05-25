
# Area of a polygon with n vertices -> Shoelace formula / Determinant of Gauss
# A = 0.5*(det|[[x1 x2][y1 y2]]| + det|[[x2 x3][y2 y3]]| + ... + det|[[xN x1][yN y1]]|)
#   = 0.5*(x1*y2-x2*y1 + x2*y3-x3*y2 + ... + xN*y1-x1*yN)
from math import sqrt
N = int(input())
coordinates = [[float(x) for x in input().split()] for i in range(N)]
A = int(input())

min_x = min([x for x,y in coordinates])
min_y = min([y for x,y in coordinates])
coordinates = [[x-min_x, y-min_y] for x,y in coordinates]

Area = 0
Area += 0.5*sum([(coordinates[i][0]*coordinates[(i+1)%N][1]) - \
            (coordinates[i][1]*coordinates[(i+1)%N][0]) for i in range(N)])
A_change = sqrt(A/Area)
coordinates = [[x*A_change, y*A_change] for x,y in coordinates]
for x,y in coordinates:
    print(x, y)
