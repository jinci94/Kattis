n, m = [int(x) for x in input().split()]
X = {x:1 for x in input().split()}
for i in range(n-1):
    Y = list(set(input().split()))
    for y in Y:
        if y in X:
            X[y] += 1
items = sorted([a for (a,b) in list(X.items()) if b==n])
print(len(items))
for item in items:
    print(item)
