x = [int(x) for x in input().split()]
n = x[0]; a = x[1:]

def p(x):
    return sum([ai*x**(n-i) for i, ai in enumerate(a)])

def Pascals_triangle(i):
    temp_pascal = [1]
    for j in range(i):
        temp_pascal = [0] + temp_pascal + [0]
        temp_pascal = [temp_pascal[k]+temp_pascal[k+1] for k in range(j+2)]
    return temp_pascal

C = [p(0)]
for i in range(1,n+1):
    C_i = p(i) - sum([c*p for c, p in zip(C,Pascals_triangle(i)[:-1])])
    C.append(C_i)
    
print(' '.join([str(c) for c in C]))