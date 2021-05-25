import re

def molecular_structure(temp):
    have = {}
    for i, c in enumerate(temp):
        if c.isalpha():
            if len(c) == 1 and i != len(temp)-1:
                if c not in have:
                    have[c] = int(temp[i+1])
                else:
                    have[c] += int(temp[i+1])
            elif len(c) == 1:
                if c not in have:
                    have[c] = 1
                else:
                    have[c] += 1
            else:
                for d in c[:-1]:
                    if d not in have:
                        have[d] = 1
                    else:
                        have[d] += 1
                d = c[-1]
                if i != len(temp)-1:
                    if d not in have:
                        have[d] = int(temp[i+1])
                    else:
                        have[d] += int(temp[i+1])
                else:
                    if d not in have:
                        have[d] = 1
                    else:
                        have[d] += 1
    return have

first_line = input().split()
second_line = input()
N = int(first_line[1])
temp1 = re.findall(r'(\d+|[A-Z]+)', first_line[0])
temp2 = re.findall(r'(\d+|[A-Z]+)', second_line)
have = {a:b*N for a,b in list(molecular_structure(temp1).items())}
want = molecular_structure(temp2)

count = 1e10
for atom in want:
    if atom not in have:
        count = 0
        break
    else:
        amount = have[atom]//want[atom]
        if amount < count:
            count = amount
print(count)