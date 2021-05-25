T = int(input())
for i in range(T):
    sound = input().split()
    animal = input()
    fox = 'what does the fox say?'
    while animal != fox:
        animal = animal.split()
        while animal[-1] in sound:
            sound.remove(animal[-1])
        animal = input()
    print(' '.join(sound))
