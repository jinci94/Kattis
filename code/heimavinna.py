N = input().split(';')
count = 0
for n in N:
    if '-' in n:
        a, b = n.split('-')
        count += int(b)-int(a)+1
    else:
        count += 1
print(count)
