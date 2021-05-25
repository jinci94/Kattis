#      N       y
#      ^       ^
#      |       |
# W <-- -->E   |
#      |      -|-------> x
#      v
#      S

# Passed 2/2:
"""
Det som jag tror gjorde att denna fungerade och inte de andra
var att jag här använde mig av set "{}" istället för listor "[]"
som varken tar med dubletter och verkar köra snabbare.
"""

order = ['N', 'E', 'S', 'W']
change = {'F':0, 'B':2, 'R':1, 'L':3}
new_coordinates = {'N': lambda x,y: (x,y-1),
                  'E': lambda x,y: (x+1,y),
                  'S': lambda x,y: (x,y+1),
                  'W': lambda x,y: (x-1,y)}
N = int(input())
print(N)
for i in range(N):
    path = input()
    coordinates = {(0,0)}
    min_x = 0; min_y = 0
    max_x = 0; max_y = 0
    last_coord = (0,0); last_dir = 'E'
    for next_step in path:
        last_dir = order[(order.index(last_dir)+change[next_step])%4]
        last_coord = new_coordinates[last_dir](*last_coord)
        coordinates.add(last_coord)
        if min_x > last_coord[0]:
            min_x = last_coord[0]
        elif max_x < last_coord[0]:
            max_x = last_coord[0]
        if min_y > last_coord[1]:
            min_y = last_coord[1]
        elif max_y < last_coord[1]:
            max_y = last_coord[1]


    print(max_y-min_y+3, max_x-min_x+2)
    for j in range(max_y-min_y+3):
        line = ''
        for i in range(max_x-min_x+2):
            line += '.' if ((i+min_x,j+min_y-1) in coordinates) else '#'
        print(line)


"""
# Passed 1/2: Time Limit Exceeded

order = ['N', 'E', 'S', 'W']
change = {'F':0, 'B':2, 'R':1, 'L':3}
new_coordinates = {'N': lambda x,y: [x,y-1],
                  'E': lambda x,y: [x+1,y],
                  'S': lambda x,y: [x,y+1],
                  'W': lambda x,y: [x-1,y]}
N = int(input())
print(N)
for i in range(N):
    path = input()
    coordinates = [[0,0]]
    last_coord = [0,0]; last_dir = 'E'
    for next_step in path:
        last_dir = order[(order.index(last_dir)+change[next_step])%4]
        last_coord = new_coordinates[last_dir](*last_coord)
        coordinates.append(last_coord)

    all_x = [x for x,y in coordinates]
    all_y = [y for x,y in coordinates]
    min_x = min(all_x); min_y = min(all_y)
    max_x = max(all_x); max_y = max(all_y)
    print(max_y-min_y+3, max_x-min_x+2)
    for j in range(max_y-min_y+3):
        print(''.join(['#' if ([i+min_x,j+min_y-1] not in coordinates) else '.' for i in range(max_x-min_x+2)]))

"""

"""
# Passed 1/2: Time Limit Exceeded
order = ['N', 'E', 'S', 'W']
change = {'F':0, 'B':2, 'R':1, 'L':3}
new_coordinates = {'N': lambda x,y: [x,y-1],
                  'E': lambda x,y: [x+1,y],
                  'S': lambda x,y: [x,y+1],
                  'W': lambda x,y: [x-1,y]}
N = int(input())
print(N)
for i in range(N):
    path = input()
    coordinates = [[0,0]]
    last_coord = [0,0]; last_dir = 'E'
    for next_step in path:
        last_dir = order[(order.index(last_dir)+change[next_step])%4]
        last_coord = new_coordinates[last_dir](last_coord[0], last_coord[1])
        #if new_coord not in coordinates:
        coordinates.append(last_coord)

    all_x = [x for x,y in coordinates]
    all_y = [y for x,y in coordinates]
    min_x = min(all_x); min_y = min(all_y)
    max_x = max(all_x); max_y = max(all_y)
    matrix = [['#' if ([i+min_x,j+min_y-1] not in coordinates) else '.' for i in range(max_x-min_x+2)] for j in range(max_y-min_y+3)]
    
    print(max_y-min_y+3, max_x-min_x+2)
    for line in matrix:
        print(''.join(line))
"""


"""
# Passed 1/2: Time Limit Exceeded

def step(this, next, dir):
    ''' dir: [x,y], next: F/R/L/B, dir: N/W/S/E
        return next coor: [x,y],  next dir: N/W/E/S'''
    x, y = this
    if dir == 'N':
        if next == 'F':
            return [x, y-1], 'N'
        elif next == 'B':
            return [x, y+1], 'S'
        elif next == 'R':
            return [x+1, y], 'E'
        elif next == 'L':
            return [x-1, y], 'W'
    elif dir == 'S':
        if next == 'F':
            return [x, y+1], 'S'
        elif next == 'B':
            return [x, y-1], 'N'
        elif next == 'R':
            return [x-1, y], 'W'
        elif next == 'L':
            return [x+1, y], 'E'
    elif dir == 'E':
        if next == 'F':
            return [x+1, y], 'E'
        elif next == 'B':
            return [x-1, y], 'W'
        elif next == 'R':
            return [x, y+1], 'S'
        elif next == 'L':
            return [x, y-1], 'N'
    elif dir == 'W':
        if next == 'F':
            return [x-1, y], 'W'
        elif next == 'B':
            return [x+1, y], 'E'
        elif next == 'R':
            return [x, y-1], 'N'
        elif next == 'L':
            return [x, y+1], 'S'


N = int(input())
print(N)
for i in range(N):
    path = input()
    coordinates = [[0,0]]
    last_coord = [0,0]; last_dir = 'E'
    for next_dir in path:
        new_coord, last_dir = step(last_coord, next_dir, last_dir)
        if new_coord not in coordinates:
            coordinates.append(new_coord)
        last_coord = new_coord
    all_x = [x for x,y in coordinates]
    all_y = [y for x,y in coordinates]
    min_x = min(all_x); min_y = min(all_y)
    max_x = max(all_x) - min_x
    max_y = max(all_y) - min_y
    modified_coord = [[x-min_x, y-min_y] for x,y in coordinates]
    matrix = [['#' for i in range(max_x+2)] for j in range(max_y+3)]
    for x,y in modified_coord:
        matrix[y+1][x] = '.'
    print(max_y+3, max_x+2)
    for line in matrix:
        print(''.join(line))
"""
