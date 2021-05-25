P, T = [int(x) for x in input().split()]
count = 0
for i in range(P):
    passed = True
    for j in range(T):
        if not input()[1:].islower():
            passed = False
    if passed:
        count += 1
print(count)