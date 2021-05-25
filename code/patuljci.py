dwarves = [int(input()) for i in range(9)]
all_sum = sum(dwarves)

for d in dwarves:
    if all_sum - 100 - d == d or all_sum - 100 - d not in dwarves:
        print(d)


"""
for d in dwarves:
    if all_sum - 100 - d in dwarves:
        dwarves.remove(d)
        dwarves.remove(all_sum-100-d)
        break
for d in dwarves:
    print(d)
"""