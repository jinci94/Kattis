want = [1, 1, 2, 2, 2, 8]
have = [int(x) for x in input().split()]
need = [w-h for w, h in zip(want, have)]
string = ''
for x in need:
    string += str(x) + ' '
print(string[:-1])
