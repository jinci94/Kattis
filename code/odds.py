from math import gcd
def posibility_winning(s0,s1,r0,r1):
    s0 = [s0] if s0 != '*' else [1,2,3,4,5,6]
    s1 = [s1] if s1 != '*' else [1,2,3,4,5,6]
    r0 = [r0] if r0 != '*' else [1,2,3,4,5,6]
    r1 = [r1] if r1 != '*' else [1,2,3,4,5,6]

    s = []
    for s00 in s0:
        for s11 in s1:
            s.append([s00, s11])
    r = []
    for r00 in r0:
        for r11 in r1:
            r.append([r00, r11])
    S = [[max(si), min(si)] for si in s]
    R = [[max(ri), min(ri)] for ri in r]

    total = len(s)*len(r)
    winning = 0
    for s in S:
        for r in R:
            if r == [2,1]:
                pass
            elif s == [2,1]:
                winning += 1
            elif s == [s[0]]*2:
                if r != [r[0]]*2:
                    winning += 1
                elif s[0] > r[0]:
                    winning += 1
            elif r == [r[0]]*2:
                pass
            elif int(str(s[0])+str(s[1])) > int(str(r[0])+str(r[1])):
                winning += 1
    if winning == 0:
        return '0'
    elif winning == total:
        return '1'
    divider = gcd(winning, total)
    return f'{winning//divider}/{total//divider}'

    

x = [int(x) if x != '*' else '*' for x in input().split()]
while x != [0]*4:
    s0,s1,r0,r1 = x
    print(posibility_winning(s0,s1,r0,r1))
    x = [int(x) if x != '*' else '*' for x in input().split()]

