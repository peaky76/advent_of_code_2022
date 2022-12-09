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
    if x_diff <= 1 and y_diff <= 1:
        pass
    elif ty == hy:
        tx = hx - 1 if hx > tx else hx + 1
    elif tx == hx:
        ty = hy - 1 if hy > ty else hy + 1
    elif x_diff < y_diff:
        tx = hx
        ty = hy - 1 if hy > ty else hy + 1
    elif x_diff > y_diff:
        tx = hx - 1 if hx > tx else hx + 1
        ty = hy
    else:
        tx = hx - 1 if hx > tx else hx + 1
        ty = hy - 1 if hy > ty else hy + 1
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
            # print(locs)
            yield locs[-1]   

def count_distinct_locs(source, chain_links_n = 1, start = (0,0)):
    return len(list(set(trace_path(source, chain_links_n, start))))

input = Input()

# TESTS
# assert(change_t_loc((1, 1), (1, 1)) == (1, 1))
# assert(change_t_loc((1, 1), (2, 1)) == (1, 1))
# assert(change_t_loc((1, 1), (1, 2)) == (1, 1))
# assert(change_t_loc((1, 1), (3, 1)) == (2, 1))
# assert(change_t_loc((1, 4), (1, 2)) == (1, 3))
# assert(change_t_loc((1, 1), (2, 3)) == (2, 2))
# assert(change_t_loc((1, 1), (3, 2)) == (2, 2))

# PART ONE
print(count_distinct_locs(input.example))
print(count_distinct_locs(input.puzzle))

# PART TWO
print(count_distinct_locs(input.example, 9))
print(count_distinct_locs(input.bonus, 9))
print(count_distinct_locs(input.puzzle, 9))