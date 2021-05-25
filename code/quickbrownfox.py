N = int(input())

for i in range(N):
    alphabet = [x for x in 'abcdefghijklmnopqrstuvwxyz']
    x = input()
    for c in x:
        if c.lower() in alphabet:
            alphabet.remove(c.lower())
    print('pangram') if len(alphabet) == 0 else print('missing', ''.join(alphabet))
        
