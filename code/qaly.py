N = int(input())
count = 0
for i in range(N):
    q, y = [float(x) for x in input().split()]
    count += q*y
print(count)

"""
5
1.0 12.0
0.7 5.2
0.9 10.7
0.5 20.4
0.2 30.0

=41.470
"""
