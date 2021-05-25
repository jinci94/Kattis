C = float(input())
L = int(input())
cost = 0
for i in range(L):
    w, l = [float(x) for x in input().split()]
    cost += w*l * C
print(cost)
