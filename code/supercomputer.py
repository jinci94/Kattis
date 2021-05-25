class supercomputer: # This is a Fenwick Tree
    def __init__(self, N):
        self.bits = [False]*N
        self.N = N
        self.sum_tree = [0] * (self.N + 1)

    def F(self, i):
        value = -1 if self.bits[i-1] else 1
        self.bits[i-1] = not self.bits[i-1]
        while i <= self.N:
            self.sum_tree[i] += value
            i += i & (-i)

    def C(self, l, r):
        return self._C(r) - (self._C(l-1) if l > 1 else 0)

    def _C(self, i):
        s = 0
        while i > 0:
            s += self.sum_tree[i]
            i -= i & (-i) 
        return s

N, K = map(int,input().split())
ft = supercomputer(N)
for _ in range(K):
    line = input().split()
    if line[0] == 'F':
        ft.F(int(line[1]))
    elif line[0] == 'C':
        print(ft.C(int(line[1]),int(line[2])))

"""
# passed 8/13

import sys

class supercomputer:
    def __init__(self, N):
        self.N = N
        self.bits = [0]*N
        self.sum = [0]*(N+1)

    def print_bits(self):
        print(self.bits)
        print(self.sum)
    
    def F(self, i):
        #self.bits[i] = 1 - self.bits[i]
        if self.bits[i] == 0:
            self.bits[i] = 1
            for j in range(i+1):
                self.sum[j] += 1
        elif self.bits[i] == 1:
            self.bits[i] = 0
            for j in range(i+1):
                self.sum[j] -= 1
    
    def C(self, l, r):
        print(self.sum[l] - self.sum[r+1])


N, K = [int(x) for x in input().split()]
sc = supercomputer(N)
for _ in range(K):
    line = sys.stdin.readline().strip().split()
    if line[0] == 'F':
        sc.F(int(line[1])-1)
    elif line[0] == 'C':
        sc.C(int(line[1])-1, int(line[2])-1)
    #sc.print_bits()
"""

"""
# passed 3/13

import sys
N, K = [int(x) for x in input().split()]
bits = [0]*N

for _ in range(K):
    line = sys.stdin.readline().strip().split()
    if line[0] == 'F':
        bits[int(line[1])-1] = 1 - bits[int(line[1])-1]
    elif line[0] == 'C':
        print( sum( bits[ int(line[1])-1 : int(line[2]) ] ))
        #print(bits[int(line[1])-1]) if line[1]==line[2] else print( sum( bits[ int(line[1])-1 : int(line[2]) ] ))
        #print( sum( bits[:int(line[2])] ) - sum( bits[:int(line[1])-1] ))
        #print( sum(bits) - sum(bits[:int(line[1])-1]) - sum(bits[int(line[2]):]) )
"""

"""
# passed 1/13

N, K = [int(x) for x in input().split()]
bits = [0]*N
change = {0:1, 1:0}
for _ in range(K):
    line = input().split()
    if line[0] == 'F':
        bits[int(line[1])] = change[bits[int(line[1])]]
    elif line[0] == 'C':
        print( sum( bits[ int(line[1]) : int(line[2])+1 ] ))
"""
