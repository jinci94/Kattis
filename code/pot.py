N = int(input())
count = 0
for i in range(N):
    line = input()
    p = int(line[-1])
    n = int(line[:-1])
    count += n**p
print(count)













"""
N = int(input())
count = 0
for i in range(N):
    P = input()
    n, p = int(P[:-1]), int(P[-1])
    count += n**p
print(count)


2
212
1253
=1953566

5
23
17
43
52
22
=102
"""