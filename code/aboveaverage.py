N = int(input())

for i in range(N):
    x = [int(x) for x in input().split()]
    people = x[0]
    grades = x[1:]
    average = sum(grades)/people
    above_average = 100*len([grade for grade in grades if grade>average])/people
    print(f'{above_average:.3f}%')
