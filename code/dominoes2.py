# first:  passed 2/4
# second: changed so one tile could push down more than one tile (4/4 passed)

N = int(input())
for i in range(N):
    n, m, l = [int(x) for x in input().split()]
    domino_effect = {i+1: [] for i in range(n)}
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        domino_effect[x] += [y]
    fallen = []
    for j in range(l):
        tile  = int(input())
        if tile not in fallen:
            fallen.append(tile)
            tiles = domino_effect[tile]
            while len(tiles) != 0 and any(t not in fallen for t in tiles):
                temp_tiles = []
                for t in tiles:
                    if t not in fallen:
                        fallen.append(t)
                        temp_tiles += domino_effect[t]
                tiles = temp_tiles
                        
    print(len(fallen))
