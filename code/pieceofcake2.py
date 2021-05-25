n, h, v = [int(x) for x in input().split()]

H = max(h, n-h)
V = max(v, n-v)
print(H*V*4)
