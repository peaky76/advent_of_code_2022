import sys

sys.path.append("..")
from input import Input

def parse_instruction(line):
    direction, num = line.split(' ')
    num = int(num) if direction in ['R', 'U'] else -int(num)
    axis = 'x' if direction in ['U', 'D'] else 'y'
    return (axis, num)    

def change_t_loc(t_loc_tuple, h_loc_tuple):
    tx, ty = t_loc_tuple
    hx, hy = h_loc_tuple
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
    else:
        tx = hx - 1 if hx > tx else hx + 1
        ty = hy
    return (tx, ty)

def trace_path(instruction_list, start = (0,0)):
    path = [start]
    t_loc_tuple = start
    h_loc_tuple = start
    for instruction in [parse_instruction(line) for line in instruction_list]:
        step = -1 if instruction[1] < 1 else 1
        for i in range(0, instruction[1], step):
            if instruction[0] == 'x':            
                h_loc_tuple = (h_loc_tuple[0] + step, h_loc_tuple[1])
            else:
                h_loc_tuple = (h_loc_tuple[0], h_loc_tuple[1] + step)    
            t_loc_tuple = change_t_loc(t_loc_tuple, h_loc_tuple)
            path.append(t_loc_tuple)    
    return path

input = Input()

# TESTS
assert(change_t_loc((1, 1), (1, 1)) == (1, 1))
assert(change_t_loc((1, 1), (2, 1)) == (1, 1))
assert(change_t_loc((1, 1), (1, 2)) == (1, 1))
assert(change_t_loc((1, 1), (3, 1)) == (2, 1))
assert(change_t_loc((1, 4), (1, 2)) == (1, 3))
assert(change_t_loc((1, 1), (2, 3)) == (2, 2))
assert(change_t_loc((1, 1), (3, 2)) == (2, 2))

# PART ONE
# print(len(list(set(trace_path(input.example)))))
print(len(list(set(trace_path(input.puzzle)))))

# PART TWO
