lines = [input() for i in range(5)]
x = ''
for i, line in enumerate(lines):
    if 'FBI' in line:
        x += str(i+1) + ' '
print('HE GOT AWAY!') if len(x) == 0 else print(x[:-1])
