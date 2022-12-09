import sys

sys.path.append("..")
from input import Input

def parse_instruction(line):
    direction, num = line.split(' ')
    num = int(num) if direction in ['R', 'U'] else -int(num)
    axis = 'y' if direction in ['U', 'D'] else 'x'
    return (axis, num)    

def change_t_loc(t_loc, h_loc):
    tx, ty = t_loc
    hx, hy = h_loc
    x_diff = abs(tx - hx)
    y_diff = abs(ty - hy)
    x_adjacent = hx - 1 if hx > tx else hx + 1
    y_adjacent = hy - 1 if hy > ty else hy + 1
    
    if x_diff <= 1 and y_diff <= 1:
        pass
    else:    
        if x_diff >= y_diff or ty == hy:
            tx = x_adjacent
        elif ty != hy:
            tx = hx

        if x_diff <= y_diff or tx == hx:
            ty = y_adjacent
        elif tx != hx:
            ty = hy
            
    return (tx, ty)

def trace_path(instruction_list, chain_links_n, start):
    locs = [start] * (chain_links_n + 1)
    for instruction in [parse_instruction(line) for line in instruction_list]:
        step = -1 if instruction[1] < 1 else 1
        for i in range(0, instruction[1], step):
            if instruction[0] == 'x':            
                locs[0] = (locs[0][0] + step, locs[0][1])
            else:
                locs[0] = (locs[0][0], locs[0][1] + step)    
            for i, loc in enumerate(locs[1:]):
                locs[i + 1] = change_t_loc(loc, locs[i])
            yield locs[-1]   

def count_distinct_locs(source, chain_links_n = 1, start = (0,0)):
    return len(list(set(trace_path(source, chain_links_n, start))))

input = Input()

# PART ONE
# print(count_distinct_locs(input.example))
print(count_distinct_locs(input.puzzle))

# PART TWO
# print(count_distinct_locs(input.example, 9))
# print(count_distinct_locs(input.bonus, 9))
print(count_distinct_locs(input.puzzle, 9))