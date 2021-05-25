N = int(input())
fac = 1
for i in range(1,N+1):
    fac *= i
    while fac % 10 == 0:
        fac //= 10
    fac %= 1000000000000    # to make the code go faster, but still give correct answers. (testade mig fram)
fac = str(fac%1000)
print(fac) if (N < 7 or len(fac) == 3) else print('0'*(3-len(fac))+fac)

#fac = str(fac)
#print(fac[max(0, len(fac)-3):])
"""
fac = 1
for i in range(N):
    fac *= i+1

nr = str(fac); i = len(nr)-1
while nr[i] == '0' and i < len(nr):
    i -= 1
print(nr[max(0, i-2): i+1])
"""

