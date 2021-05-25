W = int(input())
N = int(input())
count = 0
for i in range(N):
    w,l = [int(x) for x in input().split()]
    count += w*l
print(int(count/W))

"""
4
7
2 3
1 4
1 2
1 2
2 2
2 2
2 1

=6
"""