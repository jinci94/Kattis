X = int(input())
N = int(input())
count = X*(N+1)
for x in range(N):
    count -= int(input())

print(count)


"""
10
3
4
6
2
=28

10
3
10
2
12
=16

15
3
15
10
20
=15
"""