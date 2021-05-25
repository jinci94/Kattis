N = int(input())
A = [int(x) for x in input().split()]
#A1_w = 594; A1_l = 841  # [mm]
A1_w = 2**(-3/4); A1_l = 2**(-1/4)  # [mm]

count = 0; tape = 0
temp_w = A1_w; temp_l = A1_l
for i,a in enumerate(A):
    if count + a*2**(-i) <= 2:
        a_need = a
        count += a*2**(-i)
    else:
        a_need = (2-count)/2**(-i)
        count = 2

    if i%2==0:
        temp_l = temp_l/2
    else:
        temp_w = temp_w/2
    tape += 2*a_need*(temp_w + temp_l)
    if count == 2:
        break

print((tape - 2*(A1_w+A1_l))/2) if count == 2 else print('impossible')


"""
# passed 3/13: Time Limit Exceeded

N = int(input())
A = [int(x) for x in input().split()]
#A1_w = 594; A1_l = 841  # [mm]
A1_w = 2**(-3/4); A1_l = 2**(-1/4)  # [mm]

count = 0; tape = 0
temp_w = A1_w; temp_l = A1_l
for i,a in enumerate(A):
    a_need = 0
    for b in range(1,a+1):
        count += 2**(-i)
        a_need = b
        if count == 2:
            break
    if i%2==0:
        temp_l = temp_l/2
    else:
        temp_w = temp_w/2
    tape += 2*a_need*(temp_w + temp_l)
    if count == 2:
        break

print((tape - 2*(A1_w+A1_l))/2) if count == 2 else print('impossible')
"""
