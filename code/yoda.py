A, B = [input() for i in range(2)]
A = max(0,len(B)-len(A))*'0'+A
B = max(0,len(A)-len(B))*'0'+B
X, Y = '', ''
for a,b in zip(A,B):
    if int(a) > int(b):
        X += a
    elif int(a) < int(b):
        Y += b
    else:
        X += a
        Y += b
print('YODA') if X == '' else print(int(X))
print('YODA') if Y == '' else print(int(Y))