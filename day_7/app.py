import sys
from collections import defaultdict

sys.path.append("..")
from input import Input

def parse(line):
    if '$' in line:
        return line.split('$ ')[-1].split('cd ')[-1]
    else:
        parts = line.split(' ')[::-1]
        return [parts[0], 0] if parts[1] == 'dir' else [parts[0], int(parts[1])]
    
def create_tree(source):
    tree = defaultdict(list)
    prev_node = '~'
    current_node = '/'
    for item in source:
        line = parse(item)
        if isinstance(line, list):
            if line[1] == 0:
                tree[current_node].append(f'{current_node}::{line[0]}')
            else:
                tree[current_node].append(line[1])
        elif line == '/':
            current_node = f'{prev_node}::/'
        elif line == '..':
            current_node = prev_node
            prev_node = '::'.join(prev_node.split('::')[:-1])
        elif line != 'ls':
            prev_node = current_node
            current_node = f'{current_node}::{line}'

    return tree

def get_folder_sizes(source):
    tree = create_tree(source)
    
    while True:
        for k, v in tree.items():
            if isinstance(v, list):
                if all(isinstance(x, int) for x in v):
                    tree[k] = sum(v)
         
        for k in list(tree):
            new_value = []
            if isinstance(tree[k], list):
                for x in tree[k]:
                    if isinstance(x, str) and isinstance(tree[x], int):
                        new_value.append(tree[x])
                    else:
                        new_value.append(x)
                tree[k] = new_value

        if all(isinstance(x, int) for x in tree.values()):
            break

    return tree

def small_folders_total(source):
    return sum(x for x in get_folder_sizes(source).values() if x <= 100000)

def smallest_deleteable_dir(source, filesystem_total = 70000000, needed_space = 30000000):
    available_space = filesystem_total - get_folder_sizes(source)['~::/']
    deletion_needed = needed_space - available_space
    return next(filter(lambda folder_size: folder_size > deletion_needed, sorted(get_folder_sizes(source).values())))

input = Input()

# PART ONE
# print(small_folders_total(input.example))
print(small_folders_total(input.puzzle))

# PART TWO
# print(smallest_deleteable_dir(input.example))
print(smallest_deleteable_dir(input.puzzle))
