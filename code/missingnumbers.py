N = int(input())
l = [int(input()) for i in range(N)]
if l[-1] == N:
    print('good job')
else:
    x = [i+1 for i in range(int(l[-1]))]
    for i in x:
        if i not in l:
            print(i)
#else:
    #x = [i+1 for i in range(int(l[-1]))]
    #diff = sorted(list((set(l)|set(x)) - (set(l)&set(x))))
    #for d in diff:
    #    print(d)
