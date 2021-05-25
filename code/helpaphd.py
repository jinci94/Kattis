N = int(input())
for i in range(N):
    x = input()
    if x == 'P=NP':
        print('skipped')
    else:
        x = x.split('+')
        print(int(x[0])+int(x[1]))