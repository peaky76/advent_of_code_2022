import sys

sys.path.append("..")
from input import Input

def get_adjacents(x, y):
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

def get_grid(source):
    grid = {}
    for i, line in enumerate(source):
        for j, letter in enumerate(line):
            if letter == 'S':
                start = (i, j)
                grid[(i, j)] = ord('a')
            elif letter == 'E':
                end = (i, j)
                grid[(i, j)] = ord('z')
            else:
                grid[(i, j)] = ord(letter)
    
    return (grid, start, end)

def do_a_dijkstra(grid, start, end, match_start_value = False):
    
    approaches = {}
    for k, v in grid.items():
        approaches[k] = [(x, y) for x, y in get_adjacents(k[0], k[1]) if v - grid.get((x, y), -99999) <= 1]

    min_steps = {end: 0}
    point = end
    visited = []
    
    while (point != start if not match_start_value else grid[point] != grid[start]):
        visited.append(point)
        for approach in approaches[point]:
            if approach not in visited:
                min_steps[approach] = min_steps[point] + 1

        unvisited = [k for k in min_steps.keys() if k not in visited]
        point = min(unvisited, key=lambda x: min_steps[x])
         
    return min_steps[point]

input = Input()

# PART ONE
# print(do_a_dijkstra(*get_grid(input.example)))
print(do_a_dijkstra(*get_grid(input.puzzle)))

# PART TWO
# print(do_a_dijkstra(*get_grid(input.example), True))
print(do_a_dijkstra(*get_grid(input.puzzle), True))