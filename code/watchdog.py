from math import sqrt
N = int(input())

def shortest(S, h):
    for i in range(S):
        for j in range(S):
            if [i,j] not in h:
                outside = False
                for (x,y) in h:
                    s = (x-i)**2 + (y-j)**2     # distance squared
                    if (i-sqrt(s) < 0 or i+sqrt(s) > S or 
                        j-sqrt(s) < 0 or j+sqrt(s) > S):
                        outside = True
                if not outside:
                    return f'{i} {j}'
    return 'poodle'

for i in range(N):
    S, H = [int(x) for x in input().split()]
    h = [[int(x) for x in input().split()] for j in range(H)]
    x = shortest(S, h)
    print(x)
    print()

# shortest leash:
"""
def shortest2(S, h):
    x = (int(S/2)+1)**2     # leash length squared
    x_cord = 0; y_cord = 0
    for i in range(S):
        for j in range(S):
            temp_x = x
            for (x,y) in h:
                s = (x-i)**2 + (y-j)**2
                if s > temp_x:
                    temp_x = s
            outside = (i-sqrt(temp_x) < 0 or i+sqrt(temp_x) > S or 
                        (j-sqrt(temp_x) < 0 or j+sqrt(temp_x) > S))
            if temp_x <= x and outside:
                if temp_x < x:
                    x = temp_x
                    x_cord = i
                    y_cord = j
                elif x_cord == i and y_cord > j:
                    y_cord = j
                elif x_cord > i:
                    x_cord = i
                    y_cord = j
    print(x)
    if x == (int(S/2)+1)**2:
        return 'poodle'
    return f'{x_cord} {y_cord}'
    """