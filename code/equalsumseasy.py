
def subset_sum(lis, subset):
    s = 0
    i = 0
    while subset > 0:
        if subset%2 == 1:
            s += lis[i]
        i += 1
        subset = subset//2
    return s

def subset_as_list(lis, x):
    lst = []
    i = 0
    while x > 0:
        if x%2 == 1:
            lst += [str(lis[i])]
        i += 1
        x = x//2
    return lst


T = int(input())
for t in range(T):
    print(f'Case #{t+1}:')
    exponential = [2**n for n in range(20)]
    lst = sorted(list(set([int(x) for x in input().split()][1:])))
    ss_map = {}; possible = False
    for i in range(3, (2**20)-1):
        if i not in exponential:
            sss = subset_sum(lst, i)
            if sss in lst:
                print(" ".join(subset_as_list(lst, i)))
                print(" ".join(subset_as_list(lst, 2**lst.index(sss))))
                possible = True
                break
            elif sss in ss_map:
                print(" ".join(subset_as_list(lst, ss_map[sss])))
                print(" ".join(subset_as_list(lst, i)))
                possible = True
                break
            else:
                ss_map[sss] = i
    if not possible:
        print("Impossible")
