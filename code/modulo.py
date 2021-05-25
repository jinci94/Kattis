x = []
for i in range(10):
    N = int(input())
    if N%42 not in x:
        x.append(N%42)
print(len(x))
