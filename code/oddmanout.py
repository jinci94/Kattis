N = int(input())
for i in range(N):
    n = int(input())
    x = [int(x) for x in input().split()]
    for c in x:
        if x.count(c) == 1:
            print(f'Case #{i+1}: {c}')