import math
h, v = [int(x) for x in input().split()]
# sin(v) = h/x -> x = h/sin(v)
l = h/math.sin(v*math.pi/180)
if l%int(l) != 0:
    print(int(l+1))
else:
    print(int(l))
