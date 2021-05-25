x = input()
per = 'PER'*int(len(x)/3)
count = 0
for c, p in zip(x, per):
    if c != p:
        count += 1
print(count)