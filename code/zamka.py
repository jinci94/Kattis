L = int(input())
D = int(input())
X = int(input())

my_range = [x for x in range(L, D+1)]

for n in my_range:
    if sum([int(i) for i in str(n)]) == X:
        print(n)
        break
for m in my_range[::-1]:
    if sum([int(i) for i in str(m)]) == X:
        print(m)
        break