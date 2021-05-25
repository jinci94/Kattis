n = int(input())
x = [int(x) for x in input().split()]

numerator = sum([i for i in x if i>=0])
denominator = sum([i for i in x if i<0]) + n

print(numerator/denominator)
