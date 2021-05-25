A, B, C, D = [int(x) for x in input().split()]
people = [int(x) for x in input().split()]

for person in people:
    count = 0
    if (person-1)%(A+B) < A:
        count += 1
    if (person-1)%(C+D) < C:
        count += 1
    print('both') if count == 2 else print('one') if count == 1 else print('none')