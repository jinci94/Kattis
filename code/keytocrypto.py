cryptic = input()
key = input()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
msg = ''
for i in range(len(cryptic)):
    a = alphabet.index(cryptic[i])
    b = alphabet.index(key[i])
    msg += alphabet[(a-b)%len(alphabet)]
    key += msg[-1]
print(msg)
