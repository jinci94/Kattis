from math import pi
D, V = [int(x) for x in input().split()]
while (D, V) != (0, 0):
    # V_cone = 2*(pi*(D/2)**2 * D/2 - pi*(d/2)**2 * d/2)/3 = pi*D**3/12 - pi*d**3/12
    # V_CYLINDER = pi*(D/2)**2 * D = pi*D**3/4
    # V_cylinder = pi*(d/2)**2 * d = pi*d**3/4
    # V = V_CYLINDER - V_cylinder - V_cone = pi*D**3/4 - pi*d**3/4 - pi*D**3/12 + pi*d**3/12
    #   = pi*D**3*(3/12 - 1/12) - pi*d**3*(3/12 - 1/12) = pi*D**3/6 - pi*d**3/6 = pi/6*(D**3-d**3)
    # ->  D**3 - 6*V/pi = d**3  ->  d = (D**3 - 6*V/pi)**(1/3)
    d = (D**3 - 6*V/pi)**(1/3)
    print(d)
    D, V = [int(x) for x in input().split()]
