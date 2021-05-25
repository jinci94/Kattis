l, r = [int(x) for x in input().split()]
print('Not a moose') if (l+r==0) else print(f'Even {l+r}') if (l==r) else print(f'Odd {2*max(l,r)}')