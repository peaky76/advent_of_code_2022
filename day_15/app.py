import re
import sys
from collections import defaultdict

sys.path.append("..")
from input import Input

def get_manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_sensors_and_beacons(source):
    sensors_and_beacons = []
    for line in source:
        line = re.sub(r'[a-zA-Z=(\s+)]', '', line)
        sensor, beacon = line.split(':')
        sensor_x, sensor_y = [int(x) for x in sensor.split(',')]
        beacon_x, beacon_y = [int(x) for x in beacon.split(',')]    
        sensors_and_beacons.append([(sensor_x, sensor_y), (beacon_x, beacon_y)])
    
    return sensors_and_beacons

def get_in_range_for_row(sensor, beacon, row):
    manhattan_distance = get_manhattan_distance(sensor, beacon)
    displacement = manhattan_distance - abs(row - sensor[1])

    return (sensor[0] - displacement, sensor[0] + displacement)

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
    sb_pairs = get_sensors_and_beacons(source)
    in_ranges = combine_ranges([get_in_range_for_row(*pair, row) for pair in sb_pairs])
    beacons_in_row = set([pair[1] for pair in sb_pairs if pair[1][1] == row])
    return sum([y - x + 1 for (x, y) in in_ranges]) - len(beacons_in_row) 

def find_missing_beacon(source, top_bound):
    sensors_and_distances = {s: get_manhattan_distance(s, b) for (s, b) in get_sensors_and_beacons(source)}

    for r in range(top_bound):
        x_in_range = []
        for sensor, distance in sensors_and_distances.items():
            displacement = distance - abs(r - sensor[1])
            if displacement >= 0:
                new_range = (max([0, sensor[0] - displacement]), min([top_bound, sensor[0] + displacement]))
                x_in_range = combine_ranges(x_in_range + [new_range])
                if x_in_range[0] == (0, top_bound):
                    break
        
        if len(x_in_range) > 1:
            missing = sorted(x_in_range)[0][1] + 1
            return (missing, r)

def calc_tuning_freq(position):
    x, y = position
    return x * 4000000 + y
    
# def draw(empties, sensors, beacons):
#     draw_dict = defaultdict(lambda: '.')
#     draw_dict.update({position: '#' for position in empties})
#     draw_dict.update({position: 'S' for position in sensors})
#     draw_dict.update({position: 'B' for position in beacons})

#     all_coords = empties + sensors + beacons
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
