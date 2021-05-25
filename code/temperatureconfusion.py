from math import gcd
a, b = [int(x) for x in input().split('/')]
A = 5*(a-32*b)
B = 9*b 
divider = gcd(A,B)
print(f'{int(A/divider)}/{int(B/divider)}')