from math import pi
r, m, c = [float(x) for x in input().split()]
while not r==m==c==0:
    print(pi*r**2, 4*r**2*c/m)
    r, m, c = [float(x) for x in input().split()]
