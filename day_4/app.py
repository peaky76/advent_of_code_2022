import sys

sys.path.append("..")
from input import Input

def count_overlaps(source, overlap_type = all):
    return sum([
        (has_overlap(*pair, overlap_type) or has_overlap(*pair[::-1], overlap_type)) 
        for pair in [get_assignments(pair) for pair in source]
    ])

def get_assignments(pair):
    return [[int(x) for x in ass.split('-')] for ass in pair.split(',')]

def has_overlap(base_ass, test_ass, overlap_type):
    return overlap_type([x in range(base_ass[0], base_ass[1] + 1) for x in test_ass])

input = Input()

# PART ONE
# print(count_overlaps(input.example))
print(count_overlaps(input.puzzle))

# PART TWO
# print(count_overlaps(input.example, any))
print(count_overlaps(input.puzzle, any))
