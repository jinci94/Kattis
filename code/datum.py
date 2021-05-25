import datetime
D, M = [int(x) for x in input().split()]
ans = datetime.date(2009, M, D)
print(ans.strftime("%A"))