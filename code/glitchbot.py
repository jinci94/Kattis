x, y = [int(x) for x in input().split()]
N = int(input())
instructions = [input() for _ in range(N)]
wrong = 'F' if instructions.count('Forward')%2 != (x+y)%2 else 'LR'

order = ['N', 'E', 'S', 'W']
new_coordinates = {'N': lambda x,y: (x,y+1),
                  'E': lambda x,y: (x+1,y),
                  'S': lambda x,y: (x,y-1),
                  'W': lambda x,y: (x-1,y)}
new_direction = {'Right': +1, 'Left': -1}
for i in range(N):
    if wrong == 'F' or (wrong == 'LR' and instructions[i] != 'Forward'):
        M = 2 if (wrong == 'F' and instructions[i] == 'Forward') else 1
        for k in range(M):
            this_coord = (0,0); this_dir = 'N'; new_instruction = None
            for j, instruction in enumerate(instructions):
                if i==j:
                    if wrong == 'F':
                        if instruction != 'Forward':
                            this_coord = new_coordinates[this_dir](*this_coord)
                            new_instruction = 'Forward'
                        else:
                            new_instruction = 'Left' if k == 0 else 'Right'
                            this_dir = order[(order.index(this_dir) + new_direction[new_instruction])%4]
                    else:
                        new_instruction = {'Right': 'Left', 'Left': 'Right'}[instruction]
                        this_dir = order[(order.index(this_dir) + new_direction[new_instruction])%4]
                else:
                    if instruction == 'Forward':
                        this_coord = new_coordinates[this_dir](*this_coord)
                    else:
                        this_dir = order[(order.index(this_dir) + new_direction[instruction])%4]
            #print(i+1, '->', this_coord)
            if this_coord == (x, y):
                print(i+1, new_instruction)
                break
        if this_coord == (x, y):
            break

    

"""
test:
2 3
6
Forward
Forward
Forward
Forward
Forward
Forward

Ska bli:
Forward
Forward
Forward
Right
Forward
Forward
"""