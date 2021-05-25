N = int(input())

harshad_number = False
while harshad_number == False:
    lst = [int(x) for x in str(N)]
    if N%sum(lst) == 0:
        harshad_number = True
        print(N)
    N += 1