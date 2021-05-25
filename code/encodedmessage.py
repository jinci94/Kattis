from math import sqrt
N = int(input())
for _ in range(N):
    x = input()
    msg = ''; s = int(sqrt(len(x)))
    for i in range(len(x)):
        index = int((i%s+1)*s - i//s) - 1
        msg += x[index]
    print(msg)

#Backwards:
"""
from math import sqrt
N = int(input())
for _ in range(N):
    x = input()
    msg = ''; s = int(sqrt(len(x)))
    for i in range(len(x)):
        index = N*(N-i%s-1)+i//s
        msg += x[index]
    print(msg)
"""
