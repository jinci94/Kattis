msg = input()

if msg[0] == 'h' and msg[-1] == 'y' and msg[1:-1] == 'e'*len(msg[1:-1]):
    print('h'+'e'*len(msg[1:-1])*2+'y')