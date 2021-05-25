n, p = [int(x) for x in input().split()]
cars = sorted([int(x) for x in input().split()])
distance = 0
for i, car in enumerate(cars):
    d = p*(i+1) + cars[0] - car # the distance I need to have to the car in front of me
    if distance < d:
        distance = d
print(distance)
