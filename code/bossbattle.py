# for each turn, choose the position two steps to the right.
# this will cut the possible seats by one each time.
# when there are only one place he could have been,
# he can only be in the closest 3 seats, so then we will bomb him
n = int(input())
print(n-2) if n > 3 else print(1)