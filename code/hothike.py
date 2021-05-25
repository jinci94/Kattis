N = int(input())
days = [int(x) for x in input().split()]
day = N; temp = max(days)+1
for i in range(1,N-1):
    if max(days[i-1], days[i+1]) < temp:
        temp = max(days[i-1], days[i+1])
        day = i
print(day, temp)