L, x = [int(x) for x in input().split()]
l = 0; count = 0
for i in range(x):
    event, p = input().split()
    if event == 'enter' and l+int(p) > L:
        count += 1
    else:
        l = l+int(p) if event=='enter' else l-int(p)
print(count)
