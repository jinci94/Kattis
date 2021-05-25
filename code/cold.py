N = int(input())
x = [int(x) for x in input().split()]
print(sum([1 for i in x if i<0]))