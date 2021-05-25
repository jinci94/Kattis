characters = input()
nop = 0
count = 0
for c in characters:
    if c.isupper():
        nop += (4 - (count)%4)%4
        count = 1
    else:
        count += 1
print(nop)