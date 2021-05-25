N = int(input())
lower = []; higher = []
while N != 0:
    statement = input()
    if statement == 'too high':
        higher.append(N)
    elif statement == 'too low':
        lower.append(N)
    elif statement == 'right on':
        if all(N < x for x in higher) and all(N > x for x in lower):
            print('Stan may be honest')
        else:
            print('Stan is dishonest')
        lower = []; higher = []
    N = int(input())



