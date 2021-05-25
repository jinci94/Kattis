N = int(input())

def area(lst): # area of any rectangular cuboid
    a, b, c = lst
    return 2*a*b + 2*a*c + 2*b*c

def prime_part(N):
    partitions = []
    i = 2; n = N
    while n != 1:
        if n%i == 0:
            partitions.append(i)
            n = n//i
        else:
            i+=1
    while len(partitions) < 3:
        partitions.append(1)
    return partitions

partitions = prime_part(N)
if len(partitions) == 3:
    print(area(partitions))
else:
    if max(partitions) > int(N**(1/3)):
        a = max(partitions)
    else:
        n = int(N**(1/3))
        while N%n != 0:
            n += 1
        a = n

    b = 0; c = 0
    bc = N//a; n = int(bc**(1/2))
    while b == 0 and c == 0:
        if bc%n == 0:
            b = bc//n
            c = bc//b
        else:
            n -= 1
    partitions = [a,b,c]
    print(area(partitions))


"""
N3 = int(input())
N = int(N3**(1/3))

volume = N*N*N; area = 6*N*N
sida1 = False; sida2 = False

if not sida1 and volume+N*N <= N3:
    volume += N*N
    area += 4*N
    sida1 = True
if sida1 and not sida2 and volume+N*(N+1) <= N3:
    volume += N*(N+1)
    area += 2*N + 2*(N+1)
    sida2 = True

n = int((N3-volume)**(1/2))
volume += n*n
area += 4*n

m = N3 - volume
volume += m
if m != 0:
    if m <= n:
        area += 2
    else:
        area += 4

print(area)
"""