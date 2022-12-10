import sys

sys.path.append("..")
from input import Input

def parse_line(line):
    cycle_add = 1 if line == 'noop' else 2
    after_effect = int(line.split(' ')[1]) if ' ' in line else 0
    return (cycle_add, after_effect) 

def x_during(n, source):
    cycles = 0
    x = 1
    for line in [parse_line(line) for line in source]:
        cycles += line[0]
        if cycles >= n:
            break
        else:
            x += line[1]
    return x

def signal_strength_during(n, source):
    return n * x_during(n, source)

def draw(source):
    for i in range(0, 240):
        sprite_centre = x_during(i + 1, source)
        symbol = '#' if abs((i % 40) - sprite_centre) <= 1 else '.'
        print(symbol, end='')
        if (i + 1) % 40 == 0 and i != 0:
            print('')

input = Input()

# PART ONE
# print(sum([signal_strength_during(y, input.bonus) for y in range(20, 260, 40)]))
# print(sum([signal_strength_during(y, input.bonus) for y in range(20, 260, 40)]))
print(sum([signal_strength_during(y, input.puzzle) for y in range(20, 260, 40)]))

# PART TWO
# draw(input.bonus)
draw(input.puzzle)