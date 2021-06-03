"""
Forgot to read the information...
-> x can be negative
-> truncating integer division, so that 1/4 is 0 (instead of 0.25)
"""

N = int(input())

def test(lst):
    number = [4,4,4,4]
    i = 0
    while '*' in lst or '/' in lst:
        if lst[i]=='*':
            number[i] = number[i]*number[i+1]
            number.pop(i+1)
            lst.pop(i)
        elif lst[i]=='/':
            number[i] = number[i]//number[i+1]
            number.pop(i+1)
            lst.pop(i)
        else:
            i += 1
    i = 0
    while lst != []:
        if lst[i]=='+':
            number[i] = number[i]+number[i+1]
            number.pop(i+1)
            lst.pop(i)
        elif lst[i]=='-':
            number[i] = number[i]-number[i+1]
            number.pop(i+1)
            lst.pop(i)
        else:
            i += 1
    return number[0]

for i in range(N):
    x = int(input())
    found_solution = False
    for a in '+-*/':
        for b in '+-*/':
            for c in '+-*/':
                if test([a,b,c]) == x:
                    print(f'4 {a} 4 {b} 4 {c} 4 = {x}')
                    found_solution = True
                    break
            if found_solution:
                break
        if found_solution:
            break
    if not found_solution:
        print('no solution')

