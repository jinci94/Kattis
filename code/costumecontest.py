N = int(input())
costumes = {}
for i in range(N):
    costume = input()
    if costume not in costumes:
        costumes[costume] = 1
    else:
        costumes[costume] += 1
costumes_sorted = sorted(list(costumes.items()), key=lambda x: (x[1], x[0]))
min_part = min([e[1] for e in costumes_sorted])
i = 0
while i < len(costumes_sorted) and costumes_sorted[i][1] == min_part:
    print(costumes_sorted[i][0])
    i += 1