
nx, ny, cw = [float(x) if i==2 else int(x) for i,x in enumerate(input().split())]
L = 100; W = 75
while (nx, ny, cw) != (0, 0, 0.0):
    width = sorted([float(x) for x in input().split()])
    length = sorted([float(x) for x in input().split()])
    good_job = True
    if width[0]-cw/2 > 0 or width[-1]+cw/2 < W or length[0]-cw/2 > 0 or length[-1]+cw/2 < L:
        good_job = False
    else:
        for i in range(nx-1):
            if width[i]+cw < width[i+1]:
                good_job = False
                break
        for i in range(ny-1):
            if length[i]+cw < length[i+1]:
                good_job = False
                break
    print('YES') if good_job else print('NO')
    nx, ny, cw = [float(x) if i==2 else int(x) for i,x in enumerate(input().split())]
