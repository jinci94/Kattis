X = input().split()
N = int(input())
names = [input() for i in range(N)]
team1 = []
team2 = []
last_index = 0; first_team = True
while len(names) != 0:
    last_index = (last_index-1 + len(X))%len(names)
    if first_team:
        team1.append(names.pop(last_index))
        first_team = False
    else:
        team2.append(names.pop(last_index))
        first_team = True

for team in [team1, team2]:
    print(len(team))
    print('\n'.join(team))

