H, M = [int(x) for x in input().split()]
m = (M+60 - 45)%60
h = (H+24 + (M-45)//60)%24

print(h, m)