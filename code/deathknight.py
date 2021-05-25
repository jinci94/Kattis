N = int(input())
count = 0
for i in range(N):
    x = input()
    won = True
    for i,c in enumerate(x[:-1]):
        if c == 'C' and x[i+1] == 'D':
            won = False
    if won:
        count += 1
print(count)
