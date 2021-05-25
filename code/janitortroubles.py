from math import sqrt
x = [int(x) for x in input().split()]
s = sum(x)/2
count = 1
for xi in x:
    count *= s-xi
print(sqrt(count))