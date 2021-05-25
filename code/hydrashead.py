H, T = [int(x) for x in input().split()]
while H != 0 and T != 0:
    count = 0
    if H%2 == 1 and T == 0:
        print(-1)
    else:
        if H%2 == 0:
            while T%4 != 0:
                count += 1
                T += 1  # T -> -1 +2
            while T != 0:
                T -= 2
                H += 1
                count += 1
            while H != 0:
                H -= 2
                count += 1
        else:
            while T%4 != 2:
                count += 1
                T += 1  # T -> -1 +2
            while T != 0:
                T -= 2
                H += 1
                count += 1
            while H != 0:
                H -= 2
                count += 1
        print(count)

    H, T = [int(x) for x in input().split()]
