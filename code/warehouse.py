T = int(input())
for i in range(T):
    N = int(input())
    shipment = [input() for i in range(N)]
    toys = {}
    for s in shipment:
        toy, nr = s.split()
        if toy not in toys:
            toys[toy] = int(nr)
        else:
            toys[toy] += int(nr)
    toys_sorted = sorted(toys.items(), key=lambda x: (-x[1],x[0]), reverse=False)
    print(len(toys_sorted))
    for (toy,nr) in toys_sorted:
        print(toy, nr)