import sys
from collections import deque

sys.path.append("..")
from input import Input

def get_rearrangement(source, cratemover_version):
    details = read_input(source)
    transform = {
        9000: lambda x: x,
        9001: lambda x: x[::-1]
    }[cratemover_version]
    return ''.join([stack[-1] for stack in perform_instructions(details['instructions'], details['stacks'], transform)])

def perform_instructions(instructions, stacks, transform):
    for i in instructions:
        from_stack = stacks[i['stack_from'] - 1]
        to_stack = stacks[i['stack_to'] - 1]
        to_stack += transform([from_stack.pop() for _ in range(i['num'])])
    return stacks

def stack_level(row):
    row = row.replace('     ', ' [#] ')
    row = row.replace(']    ', '] [#]')
    row = row.replace('    [', '[#] [')
    row = row.replace('[', '').replace(']','') 
    return [x if x != '#' else None for x in row.split(' ')]

def instruction_row(row):
    num, stacks = row.strip().replace('move','').split('from')
    stack_from, stack_to = stacks.split('to') 
    return {
        'num': int(num),
        'stack_from': int(stack_from),
        'stack_to': int(stack_to)
    }

def read_input(source):
    stack_levels = []
    instructions = []
    for row in source:
        if row is None:
            continue
        elif row.strip()[0] == "[":
            stack_levels.append(stack_level(row))
        elif row[0:4] == 'move':
            instructions.append(instruction_row(row))
        else:
            stack_count = row.strip()[-1]
    stacks = list(zip(*stack_levels))
    return {
        'stack_count': stack_count,
        'stacks': [deque([item for item in stack[::-1] if item is not None]) for stack in stacks],
        'instructions': instructions
    }

input = Input()

# PART ONE
# print(get_rearrangement(input.example, 9000))
print(get_rearrangement(input.puzzle, 9000))

# PART TWO
# print(get_rearrangement(input.example, 9001))
print(get_rearrangement(input.puzzle, 9001))
