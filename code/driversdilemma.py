# Capacity [gallons], fuel loss [gallons per hour], distance [miles]:
C, X, M = [float(x) for x in input().split()]
# {speed [miles per hour]: fuel efficiency [miles per gallon]} = {A: B, ...}
speed_fuel = {int(speed):float(fuel) for speed, fuel in [input().split() for i in range(6)]}
# hours to get there:   M/A
# gallons needed:       M/B + X*M/A
possible = False
for speed in sorted(list(speed_fuel), reverse=True):
    gallons = M/speed_fuel[speed] + X*M/speed
    if gallons < C/2:
        print('YES', speed)
        possible = True
        break
if not possible:
    print('NO') 


"""
mph = 0
for speed in speed_fuel:
    gallons = M/speed_fuel[speed] + X*M/speed
    if gallons < C/2:
        mph = speed
    else:
        break
print('NO') if mph == 0 else print('YES', mph)
"""