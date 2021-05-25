n = len(input())
howl = 'AWAHOOW'
if n < 6:
    print(howl)
else:
    howl += 'OW'*(n//2)
    print(howl)
