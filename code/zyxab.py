N = int(input())
names = [input() for i in range(N)]

okay = []
for name in names:
    if len(name) >= 5 and len(set(name)) == len(name):
        okay.append(name)

if len(okay) == 0:
    print('neibb!')
else:
    okay = sorted(okay, key= lambda x: (-len(x),x), reverse=True)
    print(okay[0])
        