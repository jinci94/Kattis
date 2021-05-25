
saxophone = {
    'c': [2, 3, 4, 7, 8, 9, 10],
    'd': [2, 3, 4, 7, 8, 9],
    'e': [2, 3, 4, 7, 8],
    'f': [2, 3, 4, 7],
    'g': [2, 3, 4],
    'a': [2, 3],
    'b': [2],
    'C': [3],
    'D': [1, 2, 3, 4, 7, 8, 9],
    'E': [1, 2, 3, 4, 7, 8],
    'F': [1, 2, 3, 4, 7],
    'G': [1, 2, 3, 4],
    'A': [1, 2, 3],
    'B': [1, 2]
    }

N = int(input())

for i in range(N):
    notes = input()
    presses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
    fingers_used = []
    for note in notes:
        fingers_used_new = []
        for finger in saxophone[note]:
            if finger not in fingers_used:
                fingers_used_new.append(finger)
                presses[finger-1] += 1
            else:
                fingers_used_new.append(finger)
        fingers_used = fingers_used_new[:]

    for number in presses:
        print(number, end=' ')
    print()


"""
saxophone = {'c': [2,3,4,7,8,9,10],
             'd': [2,3,4,7,8,9],
             'e': [2,3,4,7,8],
             'f': [2,3,4,7],
             'g': [2,3,4],
             'a': [2,3],
             'b': [2],
             'C': [3],
             'D': [1,2,3,4,7,8,9],
             'E': [1,2,3,4,7,8],
             'F': [1,2,3,4,7],
             'G': [1,2,3,4],
             'A': [1,2,3],
             'B': [1,2]}

import itertools
N = int(input())
for j in range(N):
    x = input()
    x = ''.join(c[0] for c in itertools.groupby(x))
    press_button = [0 for _ in range(10)]
    for nr in saxophone[x[0]]:
        press_button[nr-1] += 1
    fingers_used = saxophone[x[0]]
    for c in x[1:]:
        this = saxophone[c]
        buttons = list(set(this) - set(fingers_used))
        for nr in buttons:
            press_button[nr-1] += 1
        fingers_used = this
    print(' '.join([str(x) for x in press_button]))

"""

"""
N = int(input())
for j in range(N):
    x = input()
    press_button = [0 for _ in range(10)]
    for nr in saxophone[x[0]]:
        press_button[nr-1] += 1
    for i,c in enumerate(x[1:], start=1):
        buttons = list(set(saxophone[c]) - set(saxophone[x[i-1]]))
        for nr in buttons:
            press_button[nr-1] += 1
    print(' '.join([str(x) for x in press_button]))


N = int(input())
for j in range(N):
    x = input()
    press_button = [0 for _ in range(10)]
    for nr in saxophone[x[0]]:
        press_button[nr-1] += 1
    for i,c in enumerate(x[1:], start=1):
        if not all(elem in saxophone[x[i-1]] for elem in saxophone[c]):
            buttons = list(set(saxophone[c]) - set(saxophone[x[i-1]]))
            for nr in buttons:
                press_button[nr-1] += 1
    print(' '.join([str(x) for x in press_button]))


N = int(input())
for j in range(N):
    x = input()
    press_button = [0 for _ in range(10)]
    for nr in saxophone[x[0]]:
        press_button[nr-1] += 1
    for i,c in enumerate(x[1:], start=1):
        for nr in saxophone[c]:
            if nr not in saxophone[x[i-1]]:
                press_button[nr-1] += 1
    print(' '.join([str(x) for x in press_button]))
"""
