N = int(input())
nr = ''
while N != 0:
    nr += str(N%2)
    N = N//2
count = 0
for i, n in enumerate(nr[::-1]):
    count += int(n)*2**i
print(count)