A = 'abcdefghijklmnopqrstuvwxyz'
B = ['@', '8', '(', '|)', '3', '#', '6', '[-]', '|', '_|', '|<', '1', '[]\/[]',
    '[]\[]', '0', '|D', '(,)', '|Z', '$', "']['", '|_|', '\/', '\/\/', '}{', '`/', '2']
assert len(A) == len(B), print('A and B have different lengths')
alphabet = {a:b for a,b in zip(A,B)}

characters = input()
message = ''
for c in characters:
    if c.lower() in A:
        message += alphabet[c.lower()]
    else:
        message += c
print(message)
