n = int(input())

for i in range(n):
    k = int(input())
    name = input()
    menu = [input() for i in range(k)]
    wanted_items = {'pea soup': False, 'pancakes': False}
    for item in menu:
        if item in wanted_items:
            wanted_items[item] = True
        if wanted_items['pea soup'] and wanted_items['pancakes']:
            print(name)
            break
    if wanted_items['pea soup'] and wanted_items['pancakes']:
        break
if not (wanted_items['pea soup'] and wanted_items['pancakes']):
    print('Anywhere is fine I guess')