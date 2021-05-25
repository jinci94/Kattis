N = int(input())
byte_list = [int(x) for x in input().split()]

def to_binary(n):
    binary = ''
    while n != 0:
        binary += str(n%2)
        n = n//2
    binary += '0'*(8-len(binary))
    return binary[::-1]

zero = {'1':'1', '0':'0'}
one = {'1':'0', '0':'1'}
change = {'0': zero, '1':one}
for byte in byte_list:
    start = to_binary(byte)
    x_1 = '0'
    x = ''
    for s in start[::-1]:
        x += change[s][x_1[-1]]
        x_1 += x[-1]
        # Same as: (together with dic's above)
        #if s == '1' and x_1[-1] == '1':
        #    x += '0'
        #elif s == '1' and x_1[-1] == '0':
        #    x += '1'
        #elif s == '0' and x_1[-1] == '1':
        #    x += '1'
        #elif s == '0' and x_1[-1] == '0':
        #    x += '0'
    print(int(x[::-1], 2), end=' ')
