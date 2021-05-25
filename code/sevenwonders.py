x = input()
cards = {'T':0, 'C':0, 'G':0}
for c in x:
    cards[c] += 1
lst = [e[1] for e in list(cards.items())]
count = sum([c**2 for c in lst]) + 7*min(lst)
print(count)