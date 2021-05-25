N = int(input())
nr = 1
while N != 0:
    zoo = {}
    for i in range(N):
        animal = input().split()[-1].lower()
        if animal not in zoo:
            zoo[animal] = 1
        else:
            zoo[animal] += 1
    print(f'List {nr}:')
    zoo = sorted(list(zoo.items()), key=lambda x:x[0])
    for e in zoo:
        print(f'{e[0]} | {e[1]}')

    N = int(input())
    nr += 1
