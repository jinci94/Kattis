N, B = input().split()
# N: A, K, Q, J, T, 9, 8, 7
# B: S, H, D, C
dominant = {'A':11, 'K':4, 'Q':3, 'J':20, 'T':10, '9':14, '8':0, '7':0}
not_dominant = {'A':11, 'K':4, 'Q':3, 'J':2, 'T':10, '9':0, '8':0, '7':0}
count = 0
for i in range(4*int(N)):
    d = input()
    if d[1] == B:
        count += dominant[d[0]]
    else:
        count += not_dominant[d[0]]
print(count)

