N = int(input())
x = [input() for i in range(N)]
count = 0
for i in range(N-1):
    if x[i] == x[i+1]:
        count += 1
print(count)
