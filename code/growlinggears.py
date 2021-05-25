N = int(input())
for i in range(N):
    n = int(input())
    T_list = []
    for j in range(n):
        a, b, c = [int(x) for x in input().split()]
        R = b/(2*a)
        T = -a*R**2 + b*R + c
        T_list.append(T)
    print(T_list.index(max(T_list))+1)
