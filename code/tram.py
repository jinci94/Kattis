"""
y = x + a
shortest distance from a point to the line: q
distance from the point to the line (vertical): p
q**2 + q**2 = p**2 -> q**2 = p**2 / 2
p = y_i - y(x_i) = y_i - x_i - a
total unusefullness = q1**2 + q2**2 + ... + qn**2
                    = ((y1-x1-a)**2 + (y2-x2-a)**2 + ... + (yn-xn-a)**2)/2
minimum unusefullness = d/da (total unusefullness) = 0
                      = (y1-x1-a) + (y2-x2-a) + ... + (yn-xn-a)
n*a  =  (y1-x1) + (y2-x2) + ... + (yn-xn)
  a  = ((y1-x1) + (y2-x2) + ... + (yn-xn))/n
"""


n = int(input())
a = 0
for i in range(n):
    x, y = [int(x) for x in input().split()]
    a += y-x
a = a/n
print(a)