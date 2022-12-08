import sys

sys.path.append("..")
from input import Input

def is_visible(matrix, x, y):
    sightlines = [
        [matrix[z][y] for z in range(0, x)],
        [matrix[z][y] for z in range(x + 1, len(matrix))],
        [matrix[x][z] for z in range(0, y)],
        [matrix[x][z] for z in range(y + 1, len(matrix[0]))]
    ]
    target = matrix[x][y]
    return any(all(tree < target for tree in sightline) for sightline in sightlines)

def exterior_trees_count(matrix):
    return (2 * len(matrix)) + (2 * (len(matrix[0]) - 2))

def interior_trees_count(matrix):
    return sum(is_visible(matrix, row, col) for row in range(1, len(matrix) - 1) for col in range(1, len(matrix[0]) - 1))

def count_visible_trees(source):
    matrix = [[int(tree) for tree in row] for row in source]
    return exterior_trees_count(matrix) + interior_trees_count(matrix)

input = Input()

# PART ONE
# print(count_visible_trees(input.example))
print(count_visible_trees(input.puzzle))


# PART TWO