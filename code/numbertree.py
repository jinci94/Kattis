# took 0.06 seconds:
from itertools import product
line = input().split()

if len(line) == 2:
    H, path = line
    nr = 2**(int(H)+1)-1
    before = 2**(len(path))-1
    binary = ''
    for c in path:
        if c == 'L':
            binary += '0'
        else:
            binary += '1'
    this = int(binary, 2)   # from binary to decimal
    print(nr-before-this)
elif len(line) == 1:
    print(2**(int(line[0])+1)-1)

"""
# Almost made it: (passed 23/29 test cases)

from itertools import product

line = input().split()

if len(line) == 2:
    H, path = line
    nr = 2**(int(H)+1)-1
    before = 2**(len(path))-1
    tree = [''.join(i) for i in product(['L', 'R'], repeat = len(path))]
    print(nr-before-tree.index(path))

elif len(line) == 1:
    print(2**(int(line[0])+1)-1)
"""

"""
# took too long... (passed 4/29 test cases) 
# (same with itertools, which I tried after)

def possible_comb(L):
    binary = []
    for i in range(2**L):
        if i <= 1:
            binary.append('0'*(L-1) + str(i))
        else:
            temp_binary = ''
            temp_i = i
            while temp_i != 0:
                temp_binary += str(temp_i%2)
                temp_i = temp_i//2
            binary.append('0'*(L-len(temp_binary)) + temp_binary[::-1])
    LR = []
    LR_dir = {'0':'L', '1': 'R'}
    for comb in binary:
        temp_LR = ''
        for c in comb:
            temp_LR += LR_dir[c]
        LR.append(temp_LR)
    return LR
# -----------------------------------------------------
line = input().split()
if len(line) == 2:
    H, path = line
elif len(line) == 1:
    H, path = line[0], 'start'
else:
    print('Error!')

nr = 2**(int(H)+1)-1
tree = {'start':nr}
for i in range(1,int(H)+1):
    LR = possible_comb(i)
    for comb in LR:
        nr -= 1
        tree[comb] = nr

print(tree[path])
"""