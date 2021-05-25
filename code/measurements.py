# def from_to(value): return changed_value
# if we go from lea to th, then n=True

def th(x, name, n):
    if name == 'th':
        return x
    if not n:
        return inc(x/1000, name, n)

def inc(x, name, n):
    if name == 'in':
        return x
    if n:
        return th(x*1000, name, n)
    else:
        return ft(x/12, name, n)

def ft(x, name, n):
    if name == 'ft':
        return x
    if n:
        return inc(x*12, name, n)
    else:
        return yd(x/3, name, n)

def yd(x, name, n):
    if name == 'yd':
        return x
    if n:
        return ft(x*3, name, n)
    else:
        return ch(x/22, name, n)

def ch(x, name, n):
    if name == 'ch':
        return x
    if n:
        return yd(x*22, name, n)
    else:
        return fur(x/10, name, n)

def fur(x, name, n):
    if name == 'fur':
        return x
    if n:
        return ch(x*10, name, n)
    else:
        return mi(x/8, name, n)

def mi(x, name, n):
    if name == 'mi':
        return x
    if n:
        return fur(x*8, name, n)
    else:
        return lea(x/3, name, n)

def lea(x, name, n):
    if name == 'lea':
        return x
    if n:
        return mi(x*3, name, n)

# =====================================================================================

names = {'thou':'th', 'th':'th',
         'inch':'in', 'in':'in',
         'foot':'ft', 'ft':'ft',
         'yard':'yd', 'yd':'yd',
         'chain':'ch', 'ch':'ch',
         'furlong':'fur', 'fur':'fur',
         'mile':'mi', 'mi':'mi',
         'league':'lea', 'lea':'lea'}

order = ['th', 'in', 'ft', 'yd', 'ch', 'fur', 'mi', 'lea']
functions = {'th':th, 'in':inc, 'ft':ft, 'yd':yd, 'ch':ch, 'fur':fur, 'mi':mi, 'lea':lea}

# =====================================================================================

n, f, _, t = input().split()
print(functions[names[f]](int(n), names[t], order.index(names[f])>order.index(names[t])))
