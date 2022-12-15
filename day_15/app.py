import re
import sys
from collections import defaultdict

sys.path.append("..")
from input import Input

def get_manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_signals_and_beacons(source):
    signals_and_beacons = []
    for line in source:
        line = re.sub(r'[a-zA-Z=(\s+)]', '', line)
        signal, beacon = line.split(':')
        signal_x, signal_y = [int(x) for x in signal.split(',')]
        beacon_x, beacon_y = [int(x) for x in beacon.split(',')]    
        signals_and_beacons.append([(signal_x, signal_y), (beacon_x, beacon_y)])
    
    return signals_and_beacons

def signals_per_beacon(sb_pairs):
    signals_per_beacon = defaultdict(list)
    for signal, beacon in sb_pairs:
        signals_per_beacon[beacon].append(signal)
    return signals_per_beacon

def get_in_range_in_row(signal, beacon, row):
    manhattan_distance = get_manhattan_distance(signal, beacon)
    displacement = manhattan_distance - abs(row - signal[1])

    return (signal[0] - displacement, signal[0] + displacement)

def combine_ranges(ranges):

    new_range_start = None
    new_range_end = None
    new_ranges = []

    for range in sorted(ranges):
  
      if new_range_start is None:
          new_range_start = range[0]
          new_range_end = range[1]
          next
      else: 
          new_range_start = min(new_range_start, range[0])

      if new_range_end < range[0] - 1:
          new_ranges.append((new_range_start, new_range_end))
          new_range_start = range[0]
          new_range_end = range[1]
      else:
          new_range_end = max(new_range_end, range[1])
        
    new_ranges.append((new_range_start, new_range_end))
  
    return new_ranges

def get_no_beacon_count(source, row):
    sb_pairs = get_signals_and_beacons(source)
    in_ranges = combine_ranges([get_in_range_in_row(*pair, row) for pair in sb_pairs])
    beacons_in_row = set([pair[1] for pair in sb_pairs if pair[1][1] == row])
    return sum([y - x + 1 for (x, y) in in_ranges]) - len(beacons_in_row) 

def find_missing_beacon(source, top_bound):
    signals_and_distances = {s: get_manhattan_distance(s, b) for (s, b) in get_signals_and_beacons(source)}

    for r in range(top_bound):
        x_in_range = []
        for signal, distance in signals_and_distances.items():
            y_delta_from_signal = abs(r - signal[1])
            manhattan_offset = distance - y_delta_from_signal
            if manhattan_offset >= 0:
                new_range = (max([0, signal[0] - manhattan_offset]), min([top_bound, signal[0] + manhattan_offset]))
                x_in_range = combine_ranges(x_in_range + [new_range])
                if x_in_range[0] == (0, top_bound):
                    break
        
        if len(x_in_range) > 1:
            missing = sorted(x_in_range)[0][1] + 1
            return (missing, r)

def calc_tuning_freq(position):
    x, y = position
    return x * 4000000 + y
    
# def draw(empties, signals, beacons):
#     draw_dict = defaultdict(lambda: '.')
#     draw_dict.update({position: '#' for position in empties})
#     draw_dict.update({position: 'S' for position in signals})
#     draw_dict.update({position: 'B' for position in beacons})

#     all_coords = empties + signals + beacons
#     min_x = min([coord[0] for coord in all_coords]) - 1
#     max_x = max([coord[0] for coord in all_coords]) + 2
#     min_y = min([coord[1] for coord in all_coords]) - 1
#     max_y = max([coord[1] for coord in all_coords]) + 2

#     for y in range(min_y, max_y):
#         for x in range(min_x, max_x):
#             print(draw_dict[(x, y)], end='')
#         print('\n')

input = Input()

# PART ONE
# print(get_no_beacon_count(input.example, 10))
print(get_no_beacon_count(input.puzzle, 2000000))

# PART TWO
# print(calc_tuning_freq(find_missing_beacon(input.example, 20)))
print(calc_tuning_freq(find_missing_beacon(input.puzzle, 4000000)))
