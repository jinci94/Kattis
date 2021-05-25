n = int(input())
while n != 0:
    ordered_items = {}
    for i in range(n):
        x = input().split()
        name = x[0]; items = x[1:]
        for item in items:
            if item not in ordered_items:
                ordered_items[item] = [name]
            else:
                ordered_items[item] += [name]
    ordered_items = {item: sorted(lst) for item, lst in list(ordered_items.items())}
    ordered_items = sorted(list(ordered_items.items()), key=lambda x:x[0])
    for e in ordered_items:
        print(e[0], ' '.join(e[1]))
    print()
    n = int(input())
