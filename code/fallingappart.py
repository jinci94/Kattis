N = int(input())
x = [int(x) for x in input().split()]
turn = [0,0]    # [A,B]
for i in range(N):
    turn[i%2] += max(x)
    x.remove(max(x))
print(turn[0], turn[1])