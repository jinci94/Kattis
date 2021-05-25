while True:
    try:
        line = input()
    except EOFError:
        break
    if line == '0': # for me to be able to stop it (instead of EOF)
        break
    n = int(line)
    ones = 1; count = 1
    #ones = int('1'*(len(line))); count = len(line)
    while ones%n != 0:
        ones = ones*10 + 1
        ones %= n
        count += 1
    
    print(count)
