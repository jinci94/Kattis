N = int(input())
if N%2==1:
    for i in range(N):
        x1 = int(input())
    print('still running')
else:
    y = 0
    for i in range(int(N/2)):
        x1 = int(input())
        x2 = int(input())
        y += x2-x1
    print(y)



"""
2
7
11
=4

5
2
5
9
10
17
=still running

4
0
2
104
117
=15
"""