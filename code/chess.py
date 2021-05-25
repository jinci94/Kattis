N = int(input())
alpha = 'ABCDEFGH'
for i in range(N):
    xa, x1, ya, y1 = input().split()
    if (alpha.index(xa) + int(x1))%2 != (alpha.index(ya) + int(y1))%2:
        print('Impossible')
    else:
        x1, y1 = int(x1), int(y1)
        if (xa, x1) == (ya, y1):
            print(0, xa, x1)
        elif abs(x1 - y1) == abs(alpha.index(xa) - alpha.index(ya)):
            print(1, xa, x1, ya, y1)
        else:
            xy1 = abs(x1-y1); xya = abs(alpha.index(xa)-alpha.index(ya))
            diff = abs(xy1 - xya)//2
            if xya < xy1:
                xy_sorted = sorted([(xa,x1), (ya,y1)], key=lambda x: x[0])  # sort by ABC...
                
                if alpha.index(xy_sorted[0][0]) - diff >= 0:
                    if xy_sorted[0][1] < xy_sorted[1][1]:
                        print(2, xa, x1, alpha[alpha.index(xy_sorted[0][0])-diff], xy_sorted[0][1]+diff, ya, y1)
                    else:
                        print(2, xa, x1, alpha[alpha.index(xy_sorted[0][0])-diff], xy_sorted[0][1]-diff, ya, y1)
                
                elif alpha.index(xy_sorted[1][0]) + diff <= 7:
                    if xy_sorted[0][1] < xy_sorted[1][1]:
                        print(2, xa, x1, alpha[alpha.index(xy_sorted[1][0])+diff], xy_sorted[1][1]-diff, ya, y1)
                    else:
                        print(2, xa, x1, alpha[alpha.index(xy_sorted[1][0])+diff], xy_sorted[1][1]+diff, ya, y1)
            
            else:
                xy_sorted = sorted([(xa,x1), (ya,y1)], key=lambda x: x[1])  # sort by 123...
                
                if xy_sorted[0][1] - diff >= 1:
                    if xy_sorted[0][0] < xy_sorted[1][0]:
                        print(2, xa, x1, alpha[alpha.index(xy_sorted[0][0])+diff], xy_sorted[0][1]-diff, ya, y1)
                    else:
                        print(2, xa, x1, alpha[alpha.index(xy_sorted[0][0])-diff], xy_sorted[0][1]-diff, ya, y1)
                
                elif xy_sorted[1][1] + diff <= 8:
                    if xy_sorted[0][0] < xy_sorted[1][0]:
                        print(2, xa, x1, alpha[alpha.index(xy_sorted[1][0])-diff], xy_sorted[1][1]+diff, ya, y1)
                    else:
                        print(2, xa, x1, alpha[alpha.index(xy_sorted[1][0])+diff], xy_sorted[1][1]+diff, ya, y1)

