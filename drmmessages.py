x = input()
# Divide:
a, b = x[:int(len(x)/2)], x[int(len(x)/2):]
# Rotate:
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
count_a = 0; count_b = 0
for i, j in zip(a, b):
    count_a += alphabet.index(i)
    count_b += alphabet.index(j)
aa, bb = '', ''
for i, j in zip(a, b):
    aa += alphabet[(alphabet.index(i)+count_a)%len(alphabet)]
    bb += alphabet[(alphabet.index(j)+count_b)%len(alphabet)]
# Merge:
msg = ''
for i, j in zip(aa, bb):
    msg += alphabet[(alphabet.index(i)+alphabet.index(j))%len(alphabet)]
print(msg)
