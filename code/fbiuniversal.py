N = int(input())
base = {x:i for i, x in enumerate('0123456789ACDEFHJKLMNPRTVWX')}
base_extra = {'B':8, 'G':'C', 'I':1, 'O':0, 'Q':0, 'S':5, 'U':'V', 'Y':'V', 'Z':2}
check = [2, 4, 5, 7, 8, 10, 11, 13]
for i in range(N):
    K, values = input().split()
    values = [base[v] if v in base else base[base_extra[v]] for v in values]
    computed_digits = sum([c*D for c, D in zip(check, values)])
    check_value = values[-1]
    if computed_digits%27 == check_value:
        decimal_value = sum([v*27**(7-i) for i,v in enumerate(values[:-1])])
        print(K, decimal_value)
    else:
        print(K, 'Invalid')

