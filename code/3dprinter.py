N = int(input())

printers = 1  
statues = 0
days = 0
while printers*2 < N:
    printers *= 2
    days += 1
while statues < N:
    statues += printers
    days += 1
print(days)

