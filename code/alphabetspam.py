x = input()
signs = [0,0,0,0]
for c in x:
    if c == '_':
        signs[0] += 1
    elif c.islower():
        signs[1] += 1
    elif c.isupper():
        signs[2] += 1
    else:
        signs[3] += 1
for sign in signs:
    print(sign/sum(signs))
