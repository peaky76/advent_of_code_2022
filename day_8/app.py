import math
import sys

sys.path.append("..")
from input import Input

def get_sightlines(matrix, x, y, direction = 'TO'):
    north, south, west, east = [
        [matrix[z][y] for z in range(x)],
        [matrix[z][y] for z in range(x + 1, len(matrix))],
        [matrix[x][z] for z in range(y)],
        [matrix[x][z] for z in range(y + 1, len(matrix[0]))]
    ]
    return [north, south[::-1], west, east[::-1]] if direction == 'TO' else [north[::-1], south, west[::-1], east]

def scenic_score(matrix, x, y):
    target = matrix[x][y]
    return math.prod([
        next((i + 1 for i, tree in enumerate(direction) if tree >= target), len(direction)) # Visible trees count 
        for direction in get_sightlines(matrix, x, y, 'FROM')
    ])    
   
def is_visible(matrix, x, y):
    target = matrix[x][y]
    return any(all(tree < target for tree in sightline) for sightline in get_sightlines(matrix, x, y, 'TO'))

def get_result(source, calc_fn, assess_fn):
    matrix = [[int(tree) for tree in row] for row in source]
    return calc_fn(assess_fn(matrix, row, col) for row in range(len(matrix)) for col in range(len(matrix[0])))

input = Input()

# PART ONE
# print(get_result(input.example, sum, is_visible))
print(get_result(input.puzzle, sum, is_visible))

# PART TWO
# print(get_result(input.example, max, scenic_score))
print(get_result(input.puzzle, max, scenic_score))