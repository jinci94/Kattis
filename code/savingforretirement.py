from math import ceil
B, Br, Bs, A, As = [int(x) for x in input().split()]
B_money = (Br - B)*Bs
# A_money = (Ar - A)*As > B_money
# Ar > B_money/As + A
# for >= we could use ceil(...) and for > we use int(... +1)
print(int(B_money/As + A + 1))