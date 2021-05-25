from math import sin, cos, pi
N = int(input())
# x(t) = v0*t*cos(theta)
# y(t) = v0*t*sin(theta) - g*t**2/2
g = 9.81
for i in range(N):
    v0, theta, x1, h1, h2 = [float(x) for x in input().split()]
    t = x1/(v0*cos(theta*pi/180))
    y = v0*t*sin(theta*pi/180) - (g*t**2)/2
    if h1+1 <= y <= h2-1:
        print('Safe')
    else:
        print('Not Safe')