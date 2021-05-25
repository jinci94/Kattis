N = int(input())
x = input().split()
makes_sense = True
for i in range(N):
    if not (x[i] == str(i+1) or x[i] == 'mumble'):
        makes_sense = False
print('makes sense') if makes_sense else print('something is fishy')