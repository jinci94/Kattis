case = 1
while True:
    try:
        line = input()
    except EOFError:
        break
    x = [int(x) for x in line.split()][1:]
    x_min = min(x); x_max = max(x)
    x_range = x_max - x_min
    print(f'Case {case}: {x_min} {x_max} {x_range}')
    case += 1
    