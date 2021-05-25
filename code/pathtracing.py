
moves = {'up': lambda x: (x[0], x[1]-1),
         'down': lambda x: (x[0], x[1]+1),
         'left': lambda x: (x[0]-1, x[1]),
         'right': lambda x: (x[0]+1, x[1])}
coordinates = [(0,0)]
min_x = 0; min_y = 0
max_x = 0; max_y = 0
while True:
    try:
        line = input()
    except EOFError:
        break
    if line == '0': # for me, so I can stop the code instead of going EOF
        break
    x, y = moves[line](coordinates[-1])
    coordinates.append((x,y))

    if x < min_x:
        min_x = x
    elif x > max_x:
        max_x = x
    if y < min_y:
        min_y = y
    elif y > max_y:
        max_y = y

width = max_x - min_x +3
height = max_y - min_y +3
print('#'*width)
for i in range(height-2):
    print('#', end='')
    for j in range(width-2):
        if (j+min_x ,i+min_y) == coordinates[0]:
            print('S', end='')
        elif (j+min_x ,i+min_y) == coordinates[-1]:
            print('E', end='')
        elif (j+min_x ,i+min_y) in coordinates:
            print('*', end='')
        else:
            print(' ', end='')
    print('#')
print('#'*width)


    