N = int(input())
lst = []; count = 0
for i in range(N):
    x = input()
    if count != 12 and x.split()[0] not in lst:
        count += 1
        lst.append(x.split()[0])
        print(x)