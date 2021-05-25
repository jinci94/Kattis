N = int(input())
x = input()
y = input()
if N%2==0:
    msg = 'succeeded' if x == y else 'failed'
else:
    x_new = ''.join(['1' if i=='0' else '0' for i in x])
    msg = 'succeeded' if x_new == y else 'failed'

print('Deletion', msg)