import math
import sys

sys.path.append("..")
from input import Input

def get_matrix(source):
    return [[int(tree) for tree in row] for row in source]

def get_sightlines(matrix, x, y):
    return [
        [matrix[z][y] for z in range(x)],
        [matrix[z][y] for z in range(x + 1, len(matrix))],
        [matrix[x][z] for z in range(y)],
        [matrix[x][z] for z in range(y + 1, len(matrix[0]))]
    ]

def get_scenic_score(matrix, x, y):
    sightlines = get_sightlines(matrix, x, y)
    target = matrix[x][y]
    north, south, west, east = sightlines
    north = north[::-1]
    west = west[::-1]
    scores = []
    for direction in [north, west, east, south]:
        score = 0
        for tree in direction:
            if tree < target:
                score +=1
            else:
                score += 1
                break
        scores.append(score)

    return math.prod(scores)    

def is_visible(matrix, x, y):
    sightlines = get_sightlines(matrix, x, y)
    target = matrix[x][y]
    return any(all(tree < target for tree in sightline) for sightline in sightlines)

def count_visible_trees(source):
    matrix = get_matrix(source)     
    return sum(is_visible(matrix, row, col) for row in range(len(matrix)) for col in range(len(matrix[0])))

def get_ideal_spot_score(source):
    matrix = get_matrix(source)
    return max(get_scenic_score(matrix, row, col) for row in range(len(matrix)) for col in range(len(matrix[0])))

input = Input()

# PART ONE
# print(count_visible_trees(input.example))
# print(count_visible_trees(input.puzzle))

# PART TWO
# print(get_ideal_spot_score(input.example))
print(get_ideal_spot_score(input.puzzle))