msg = 'Simon says '

N = int(input())
for i in range(N):
    x = input()
    if len(x)>len(msg) and x[:len(msg)] == msg:
        print(x[len(msg):])

"""
1
Simon says smile.

3
Simon says raise your right hand.
Lower your right hand.
Simon says raise your left hand.

3
Raise your right hand.
Lower your right hand.
Simon says raise your left hand.
"""