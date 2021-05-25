v = [int(x) for x in input().split()]
prime = [2, 3, 5, 7, 11, 13, 17, 19]
p = [1 for i in range(8)]
for i in range(1,8):
    for j in range(i):
        p[i] *= prime[j]
output = sum([(prime[i]-1-v[i])*p[i] for i in range(8)])
print(output)
