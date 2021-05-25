N, M = [int(x) for x in input().split()]

facit = []
for i in range(1,M+1):
    if i%3==0 and i%5==0:
        facit.append('fizzbuzz')
    elif i%3==0:
        facit.append('fizz')
    elif i%5==0:
        facit.append('buzz')
    else:
        facit.append(str(i))
        
index = 0; highest = 0
for i in range(N):
    x = input().split()
    nr_correct = sum([1 for xi, fi in zip(x, facit) if xi==fi])
    if highest < nr_correct:
        highest = nr_correct
        index = i
print(index+1)