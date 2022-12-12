import sys
from collections import deque

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
    todo = deque()
    
    while (grid[point] != grid[start] if match_start_value else point != start):
        visited.append(point)
        for approach in approaches[point]:
            if approach not in visited:
                min_steps[approach] = min_steps[point] + 1
                if approach not in todo:
                    todo.append(approach)

        point = todo.popleft()
         
    return min_steps[point]

input = Input()

# PART ONE
# print(do_a_dijkstra(*get_grid(input.example)))
print(do_a_dijkstra(*get_grid(input.puzzle)))

# PART TWO
# print(do_a_dijkstra(*get_grid(input.example), True))
print(do_a_dijkstra(*get_grid(input.puzzle), True))