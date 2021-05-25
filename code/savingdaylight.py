# Tog flera timmar att hitta felet. (klarade av första testen, men stannade på andra. totalt tre tester)
# Felet var att det inte blev rätt tid då minuterna var samma
while True:
    try:
        line = input()
    except EOFError:
        break
    M, D, Y, XX, YY = line.split()
    h1, m1 = [int(x) for x in XX.split(':')]
    h2, m2 = [int(x) for x in YY.split(':')]
    if m1 == m2:
        print(f'{M} {D} {Y} {(h2-h1)%24-(m1-m2)//60} hours {(m2-m1)%60} minutes')
    else:
        print(f'{M} {D} {Y} {(h2-h1)%24-1-(m1-m2)//60} hours {(m2-m1)%60} minutes')

"""
while True:
    try:
        line = input()
    except EOFError:
        break
    M, D, Y, XX, YY = line.split()
    h1, m1 = [int(x) for x in XX.split(':')]
    h2, m2 = [int(x) for x in YY.split(':')]
    print(f'{M} {D} {Y} {(h2-h1)%24-1-(m1-m2)//60} hours {(m2-m1)%60} minutes')
"""
#try:
#line = input()
#except EOFError:
#break