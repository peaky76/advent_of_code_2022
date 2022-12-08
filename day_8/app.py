import sys

sys.path.append("..")
from input import Input

def is_visible(matrix, x, y):
    sightlines = [
        [matrix[z][y] for z in range(x)],
        [matrix[z][y] for z in range(x + 1, len(matrix))],
        [matrix[x][z] for z in range(y)],
        [matrix[x][z] for z in range(y + 1, len(matrix[0]))]
    ]
    target = matrix[x][y]
    return any(all(tree < target for tree in sightline) for sightline in sightlines)

def count_visible_trees(source):
    matrix = [[int(tree) for tree in row] for row in source]
    return sum(is_visible(matrix, row, col) for row in range(len(matrix)) for col in range(len(matrix[0])))

input = Input()

# PART ONE
# print(count_visible_trees(input.example))
print(count_visible_trees(input.puzzle))


# PART TWO