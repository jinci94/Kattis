import sys
N, M = [int(x) for x in sys.stdin.readline().strip().split()]
while N != 0 and M != 0:
    print(N+M - len({int(sys.stdin.readline().strip()) for i in range(N+M)}))
    #Jack = {int(sys.stdin.readline().strip()) for i in range(N)}
    #Jill = {int(sys.stdin.readline().strip()) for i in range(M)}
    #double = Jack & Jill
    #print(len(double))
    N, M = [int(x) for x in sys.stdin.readline().strip().split()]

"""
Slutsats:
-> sys.stdin.readline().strip() är snabbare än input() (enl stackoverflow ca 10ggr snabbare)
-> {int(...) for i in range(N)} är snabbare än {... for i in range(N)}
(Sedan tidigare har jag även upptäckt att set, {}, är snabbare än listor)

Funkar endast med både <<sys.stdin.readline().strip()>> och <<int(...)>>, ej utan en av dessa!

Både linje 4 ovan funkar samt linjerna 5-8. Inte särskillt stor skillnad (ca 0.1s snabbare med linje 4)
"""
