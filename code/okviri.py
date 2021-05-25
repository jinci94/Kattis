x = [w for w in input()]
first = ['*' if (i+2)%12==0 else '#' if (i+2)%4==0 else '.' for i in range(4*len(x)+1)]
second = ['.' if i%2==0 else '*' if (i%12==9 or i%12==11) else '#' for i in range(4*len(x)+1)]
middle = '#'
for i in range(1,4*len(x)+1):
    if i%2 == 1:
        middle += '.'
    elif (i+2)%4 == 0:
        middle += x[(i+2)//4-1]
    elif (i+8)%12==0:
        middle += '#'
    else:
        middle += '*'
if len(x)%3==2:
    middle = middle[:-1]+'#'
print(''.join(first))
print(''.join(second))
print(middle)
print(''.join(second))
print(''.join(first))
