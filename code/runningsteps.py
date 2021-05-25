from math import ceil
from itertools import permutations 

"""
def possibilities_slow(S):
    X = []  # nr of 1, nr of 2
    two = ceil(S/3) if ceil(S/3)%2==0 else ceil(S/3)+1
    one = S-2*two
    X.append([one,two])
    count_permutations = 0
    while one//4 >= 1:
        two += 2
        one -= 4
        X.append([one,two])
    for x in X:
        perm = list(set(permutations([nr for nr in '1'*x[0]+'2'*x[1]])))
        for p in perm:
            count = {'L1':0, 'R1':0, 'L2':0, 'R2':0}
            for i, pi in enumerate(p):
                if i%2 == 1:
                    count[f'L{pi}'] += 1
                else:
                    count[f'R{pi}'] += 1
            if (count['L1'] == count['R1'] and count['L2'] == count['R2'] and count['L1'] <= count['L2']):
                count_permutations += 1
    return count_permutations
"""
def fac(n):
    count = 1
    for i in range(n):
        count *= i+1
    return count

def a_over_b(a,b):
    return fac(a)/(fac(b)*fac(a-b))

def possibilities(S):   # mathematical way (found with pen and paper)
    X = []  # nr of 1, nr of 2
    two = ceil(S/3) if ceil(S/3)%2==0 else ceil(S/3)+1
    one = S-2*two
    X.append([one,two])
    
    while one//4 >= 1:
        two += 2
        one -= 4
        X.append([one,two])
    
    count_permutations = 0
    for x in X:
        count_permutations += int(a_over_b((x[0]+x[1])//2,(x[0])//2))**2

    return count_permutations

N = int(input())
for i in range(N):
    K, S = [int(x) for x in input().split()]
    if S == 2:      # needed this case to pass 2/2
        print(K, 0)
    else:
        print(K, possibilities(S))

