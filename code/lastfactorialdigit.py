N = int(input())
for i in range(N):
    x = int(input())
    count = 1
    for j in range(1,x+1):
        count *= j
    print(int(str(count)[-1]))

