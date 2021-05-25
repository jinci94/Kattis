
start1, stop1 = ord('!'), ord('*')
start2, stop2 = ord('['), ord(']')

while True:
    try:
        n = int(input())
    except EOFError:
        break
    s = input()
    msg = ''
    for c in s:
        if start1 <= ord(c) <= stop1 or start2 <= ord(c) <= stop2:
            msg += '\\'*(2**n - 1) + c
        else:
            msg += c
    print(msg)