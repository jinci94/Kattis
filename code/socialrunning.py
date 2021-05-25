N = int(input())
x = [int(input()) for i in range(N)]
distance = [x[i]+x[(i+2)%N] for i in range(N)]
print(min(distance))