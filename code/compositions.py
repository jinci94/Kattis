def compositions(n,m,k,lex):
    if n not in lex:
        if n==0:
            return 1
        s = 0
        for i in range(n,0,-1):
            if i % k != m:
                s += compositions(n-i,m,k,lex)
        lex[n] = s
    return lex[n]

P = int(input())
for i in range(P):
    K, n, m, k = [int(x) for x in input().split()]
    print(K, compositions(n,m,k,{}))
