L, H = [int(x) for x in input().split()]

def first(c):
    return not any(x=='0' for x in str(c))

def second(c):
    digits = [x for x in str(c)]
    return len(digits) == len(list(set(digits)))

def third(c):
    digits = [int(x) for x in str(c)]
    for d in digits:
        if c%d != 0:
            return False
    return True

count = 0
for c in range(L, H+1):
    if first(c) and second(c) and third(c):
        count += 1
print(count)
