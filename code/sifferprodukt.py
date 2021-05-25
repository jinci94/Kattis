x = [i for i in input()]
while len(x) != 1:
    count = 1
    for nr in x:
        if nr != '0':
            count *= int(nr)
    x = [i for i in str(count)]
print(x[0])
