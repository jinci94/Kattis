from math import sqrt
N = int(input())
# Cosinussatsen: 
# Big:  B^2 = A^2 + C^2 - 2AC*cos(v) => cos(v) = (A^2+C^2-B^2)/(2AC)
# Half: D^2 = A^2 + (C/2)^2 - AC*cos(v)
#  =>   D^2 = A^2 + C^2/4 - (A^2+C^2-B^2)/2
#           = (2A^2 - C^2 + 2B^2)/4
L = 0
for i in range(N):
    A, B, C = [int(x) for x in input().split()]
    D = sqrt(2*A**2 + 2*B**2 - C**2)/2
    S = (A+B+C)/2
    Area = sqrt(S*(S-A)*(S-B)*(S-C))
    L += 2*Area/D
print(L)
