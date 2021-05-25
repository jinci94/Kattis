x = input()
cups = ['o', '', '']
for c in x:
    if c == 'A':
        cups[0], cups[1] = cups[1], cups[0]
    elif c == 'B':
        cups[1], cups[2] = cups[2], cups[1]
    elif c == 'C':
        cups[0], cups[2] = cups[2], cups[0]
print(cups.index('o')+1)
