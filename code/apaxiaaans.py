naaame = input()
name = str(naaame[0])
for i in range(len(naaame)-1):
    if naaame[i] != naaame[i+1]:
        name += naaame[i+1]
print(name)
