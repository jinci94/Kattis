import itertools
N = input()
numbers = list(itertools.permutations([x for x in N]))
numbers = sorted(list(set([''.join(x) for x in numbers])))
if numbers[-1] == N:
    print(0)
else:
    for i in range(len(numbers)):
        if numbers[i] == N:
            print(numbers[i+1])
            break
