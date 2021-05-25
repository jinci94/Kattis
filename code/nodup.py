words = [x for x in input().split()]
ok = True
for i, word in enumerate(words[:-1]):
    if word in words[i+1:]:
        ok = False
        break
if ok:
    print('yes')
else:
    print('no')
