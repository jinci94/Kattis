C, n = [int(x) for x in input().split()]
count = 0; possible = True
for i in range(n):
    l, e, s = [int(x) for x in input().split()] # left, entered, stayed
    count -= l
    if count < 0:
        possible = False
    count += e
    if count > C:
        possible = False
    if count < C and s > 0:
        possible = False
if count != 0:
    possible = False
print('possible') if possible else print('impossible')
