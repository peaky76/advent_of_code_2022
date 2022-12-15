import re
import sys
from collections import defaultdict

sys.path.append("..")
from input import Input

def get_signals_and_beacons(source):
    for line in source:
        line = re.sub(r'[a-zA-Z=(\s+)]', '', line)
        signal, beacon = line.split(':')
        signal_x, signal_y = [int(x) for x in signal.split(',')]
        beacon_x, beacon_y = [int(x) for x in beacon.split(',')]    
        yield([(signal_x, signal_y), (beacon_x, beacon_y)])

def get_manhattan_distance(signal, beacon):
    return abs(signal[0] - beacon[0]) + abs(signal[1] - beacon[1])

def get_positions_within_manhattan_distance(centre, manhattan_distance):
    positions = []
    for i in range(-manhattan_distance, manhattan_distance + 1):
        for j in range(-manhattan_distance, manhattan_distance + 1):
            if abs(i) + abs(j) <= manhattan_distance:
                positions.append((centre[0] + i, centre[1] + j))
    positions.remove(centre)
    return positions

def get_row_min_max_within_manhattan_distance(centre, manhattan_distance):
    positions = {}
    for i in range(-manhattan_distance, manhattan_distance + 1):
        j = manhattan_distance - abs(i)
        positions[centre[1] + i] = (centre[0] - j, centre[0] + j)
    return positions      

def get_no_beacons_count(source, row):
    empties_per_row = defaultdict(list)
    signals = []
    beacons = []
    sb_pairs = [pair for pair in get_signals_and_beacons(source)]
    
    for sb_pair in sb_pairs:
        signal, beacon = sb_pair
        signals.append(signal)
        if beacon not in beacons:
            beacons.append(beacon)
        manhattan_distance = get_manhattan_distance(signal, beacon)
        new_empty_limits = get_row_min_max_within_manhattan_distance(signal, manhattan_distance)
        for k, v in new_empty_limits.items():
            empties_per_row[k].append(v)

    # print(beacons)
    # print([(e, row) for e in convert_ranges_to_numbers(empties_per_row[row])])
    # print([e for e in convert_ranges_to_numbers(empties_per_row[row]) if (e, row) not in beacons])

    return len([e for e in convert_ranges_to_numbers(empties_per_row[row]) if (e, row) not in beacons])

def convert_ranges_to_numbers(ranges):
    return list(set([n for r in ranges for n in range(r[0], r[1] + 1)]))
    
def draw(empties, signals, beacons):
    draw_dict = defaultdict(lambda: '.')
    draw_dict.update({position: '#' for position in empties})
    draw_dict.update({position: 'S' for position in signals})
    draw_dict.update({position: 'B' for position in beacons})

    all_coords = empties + signals + beacons
    min_x = min([coord[0] for coord in all_coords]) - 1
    max_x = max([coord[0] for coord in all_coords]) + 2
    min_y = min([coord[1] for coord in all_coords]) - 1
    max_y = max([coord[1] for coord in all_coords]) + 2

    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            print(draw_dict[(x, y)], end='')
        print('\n')

input = Input()

# PART ONE
# print(get_no_beacons_count(input.example, 10))
print(get_no_beacons_count(input.puzzle, 2000000))

# PART TWO