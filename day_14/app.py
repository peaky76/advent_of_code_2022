import sys
from collections import defaultdict

sys.path.append("..")
from input import Input

SAND_ENTRY = (500, 0)

def get_pivot_points(line):
    return [(int(pivot.split(',')[0]), int(pivot.split(',')[1])) for pivot in line.split(' -> ')]

def get_rock_lines(pivot_lst):
    coords = []
    for i, pivot in enumerate(pivot_lst[:-1]):
        x1, y1 = pivot
        x2, y2 = pivot_lst[i+1]
        if x1 == x2:
            step = 1 if y2 > y1 else -1
            coords += [(x1, j) for j in range(y1, y2 + step, step)]
        else:
            step = 1 if x2 > x1 else -1 
            coords += [(j, y1) for j in range(x1, x2 + step, step)]
    return list(set(coords))

def get_all_rocks(source):
    return [loc for lst in [get_rock_lines(line) for line in [get_pivot_points(x) for x in source]] for loc in lst]

def get_block_dict(coords, has_floor = False):
    if has_floor:
        floor = max([coord[1] for coord in coords]) + 2
        block_dict = defaultdict(lambda: [floor])
    else:
        block_dict = defaultdict(list)

    for coord in coords:
        block_dict[coord[0]].append(coord[1])
    return block_dict

def draw(rock_coords, sand_coords, has_floor):
    all_coords = rock_coords + sand_coords
    min_x = min([coord[0] for coord in all_coords]) - 1
    max_x = max([coord[0] for coord in all_coords]) + 2
    min_y = min([coord[1] for coord in all_coords]) - 1
    max_y = max([coord[1] for coord in all_coords]) + 2

    symbols = defaultdict(lambda: '.')
    symbols.update({(x, y): '#' for (x, y) in rock_coords})
    symbols.update({(x, y): 'o' for (x, y) in sand_coords})

    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            if not has_floor or not y == max_y - 1: 
                print(symbols[(x, y)], end='')
            else:
                print('#', end='')
        print('\n')

def enact_freefall(coord, block_dict):
    x, y = coord
    poss_blockages = [v for v in block_dict[x] if v > y]
    if poss_blockages:
        return (x, min(poss_blockages) - 1)
    else:
        return (x, False)

def find_resting_place(entry, block_dict):
    x, y = enact_freefall(entry, block_dict)
    while True:
        new_x, new_y = enact_freefall((x - 1, y), block_dict)   
        if new_y == y:
            new_x = x
            new_x, new_y = enact_freefall((x + 1, y), block_dict)
            if new_y == y:
                new_x = x

        if x == new_x and y == new_y:
            break
        else:
            x, y = new_x, new_y

        if y is False:
            break    

    return (x, y)

def dribble_sand(cave_map, has_floor = False):
    rock_coords = get_all_rocks(cave_map)
    sand_coords = []
    block_dict = get_block_dict(rock_coords, has_floor)

    while True:
        sand_drops_to = find_resting_place(SAND_ENTRY, block_dict)
        x, y = sand_drops_to
        if y is False:
            break

        sand_coords.append(sand_drops_to)
        block_dict[x].append(y)
        if y == 0:
            break

    # draw(rock_coords, sand_coords, has_floor)
    print(len(sand_coords))

input = Input()

# PART ONE 
# dribble_sand(input.example)
dribble_sand(input.puzzle)

# PART TWO
# dribble_sand(input.example, True)
dribble_sand(input.puzzle, True)