x = input()
too_long = False
length = 2; characters = len(x)
#while not too_long:
for j in range(len(x)):
    too_long = True
    for i in range(len(x)-length+1):
        macro = x[i:i+length]
        nr = x.count(macro)
        if characters >= len(x)+length-(length-1)*nr:
            characters = len(x)+length-(length-1)*nr
            too_long = False
    length += 1
print(characters)