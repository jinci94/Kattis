a, b, c, n = [int(x) for x in input().split()]
print('YES') if (a>=1 and b>=1 and c>=1 and a+b+c>=n and n>=3) else print('NO')