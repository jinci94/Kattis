N, b = [int(x) for x in input().split()]
# tex b=3 maximum: 111 (base2) = 1000 - 1 (base2) = 2**(3+1) - 1 (base10)
print('yes') if N <= 2**(b+1)-1 else print('no')
