N = int(input())
ballons = [i+1 for i in range(N)]
gas_canisters = sorted([int(x) for x in input().split()])
fraction = 1; possible = True
for b, g in zip(ballons, gas_canisters):
    if b < g:
        possible = False
        break
    else:
        if g/b  < fraction:
            fraction = g/b
print(fraction) if possible else print('impossible')