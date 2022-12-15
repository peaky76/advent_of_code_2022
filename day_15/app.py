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

def get_empties_per_row(source):
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

    return (empties_per_row, beacons, signals)

def convert_ranges_to_numbers(ranges):
    return list(set([n for r in ranges for n in range(r[0], r[1] + 1)]))

def find_missing_beacon(source, max):
    empties, beacons, signals = get_empties_per_row(source)
    beacons_per_row = defaultdict(list)
    signals_per_row = defaultdict(list)
    for beacon in beacons:
        beacons_per_row[beacon[1]].append(beacon[0])
    for signal in signals:
        signals_per_row[signal[1]].append(signal[0])

    for i in range(max + 1):
        cannae_be_x_for_row = sorted(list(set(convert_ranges_to_numbers(empties[i]) + beacons_per_row[i] + signals_per_row[i])))
        within_range = [x for x in cannae_be_x_for_row if x >= 0 and x <= max]
        if len(within_range) != max + 1:
            j = [e for e in range(max + 1) if e not in within_range][0]
            return (j, i)

    return None 

def get_no_beacons_count(source, row):
    empties, beacons, _ = get_empties_per_row(source)
    empty_x_for_row = convert_ranges_to_numbers(empties[row])
    return len([e for e in empty_x_for_row if (e, row) not in beacons])

def calc_tuning_freq(position):
    x, y = position
    return x * 4000000 + y
    
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
# print(get_no_beacons_count(input.puzzle, 2000000))

# PART TWO
print(calc_tuning_freq(find_missing_beacon(input.example, 20)))
print(calc_tuning_freq(find_missing_beacon(input.puzzle, 4000000)))