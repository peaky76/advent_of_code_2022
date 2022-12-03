import sys

sys.path.append("..")
from input import Input

def duplicate_item(rucksack):
    midpoint = len(rucksack) // 2
    return list(set(rucksack[:midpoint]) & set(rucksack[midpoint:]))[0]

def shared_item(three_rucksacks):
    one, two, three = three_rucksacks
    return list(set(one) & set(two) & set(three))[0]

def priority_sum(rucksacks, selection_function, grouping_n = 1):
    rucksack_groups = [rucksacks[i:i + grouping_n] for i in range(0, len(rucksacks), grouping_n)] if grouping_n > 1 else rucksacks
    rucksack_items = [selection_function(rucksack_group) for rucksack_group in rucksack_groups]
    return sum([score_letter(item) for item in rucksack_items])

def score_letter(letter):
    deduction = 96 if letter == letter.lower() else 38
    return ord(letter) - deduction

input = Input()

# PART ONE 
print(priority_sum(input.example, duplicate_item))
print(priority_sum(input.puzzle, duplicate_item)) 

# PART TWO
print(priority_sum(input.example, shared_item, 3)) 
print(priority_sum(input.puzzle, shared_item, 3))