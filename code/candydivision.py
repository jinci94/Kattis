# first try:  looped through all -> time limit exceeded (passed 5/11)
# second try: looped until sqrt(N) -> passed

from math import sqrt
N2 = int(input())
N = int(sqrt(N2))
division = []
for i in range(N):
    if N2%(i+1) == 0:
        division.append(i)
        division.append(N2//(i+1)-1)
print(*sorted(list(set(division))))