N, W, H = [int(x) for x in input().split()]
match2 = W**2 + H**2
for i in range(N):
    x = int(input())
    if x**2 <= match2:
        print('DA')
    else:
        print('NE')

"""
5 3 4
3
4
5
6
7

2 12 17
21
20
"""