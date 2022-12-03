import heapq
import sys

sys.path.append("..")
from input import Input

def get_elf_max_calorie_counts(data, n = 1):
    elf_totals = []
    current_calorie_count = 0
    for food_item in data:
        if food_item:
            current_calorie_count += food_item
        else:
            elf_totals.append(current_calorie_count)
            current_calorie_count = 0
    elf_totals.append(current_calorie_count)

    return sum(heapq.nlargest(n, elf_totals))

input = Input(int)
# PART ONE
# print(get_elf_max_calorie_counts(input.example))
print(get_elf_max_calorie_counts(input.puzzle)) 

# PART TWO
# print(get_elf_max_calorie_counts(input.example, 3))
print(get_elf_max_calorie_counts(input.puzzle, 3)) 

