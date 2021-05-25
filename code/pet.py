i = 0; count = 0
for j in range(5):
    score = sum([int(x) for x in input().split()])
    if score > count:
        count = score
        i = j+1
print(i, count)
