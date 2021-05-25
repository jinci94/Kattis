G, S, C = [int(x) for x in input().split()]
cost = G*3 + S*2 + C*1
victory = 'Province' if cost>=8 else 'Duchy' if cost>=5 else 'Estate' if cost>=2 else ''
treasure = 'Gold' if cost>=6 else 'Silver' if cost>=3 else 'Copper'
OR = ' or ' if victory != '' else ''
print(f'{victory}{OR}{treasure}')